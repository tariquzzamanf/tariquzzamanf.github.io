"""Regression checks for incomplete Scholar responses and safe updates."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import sync_scholar as sync


def profile(citations='18', h='3', i10='0'):
    return '<table id="gsc_rsb_st"><tbody>' + ''.join(
        f'<tr><td><a>{label}</a></td><td class="gsc_rsb_std">{value}</td>'
        '<td class="gsc_rsb_std">0</td></tr>'
        for label, value in [('Citations', citations), ('h-index', h), ('i10-index', i10)]
    ) + '</tbody></table>'


class ScholarTests(unittest.TestCase):
    def test_all_time_column_and_zero(self):
        self.assertEqual(sync.parse_metrics(profile()), {'citations': 18, 'h_index': 3, 'i10_index': 0})

    def test_grouped_numbers_and_nested_markup(self):
        self.assertEqual(sync.parse_metrics(profile('<span>1,234</span>'))['citations'], 1234)

    def test_blanks_never_shift_the_column(self):
        for value in ['', '—', '-1', 'unknown', '1,2']:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                sync.parse_metrics(profile(value))

    def test_blocked_or_partial_response(self):
        for page in ['<html>Verify you are human</html>', profile().replace('i10-index', 'other')]:
            with self.assertRaises(RuntimeError):
                sync.parse_metrics(page)

    def test_unrelated_tables_are_ignored(self):
        self.assertEqual(sync.parse_metrics('<td class="gsc_rsb_std">999</td>' + profile())['citations'], 18)

    def test_dry_run_and_failure_preserve_previous_bytes(self):
        with tempfile.TemporaryDirectory(prefix='.test-scholar-', dir=sync.ROOT) as directory:
            path = Path(directory) / 'metrics.json'
            previous = b'{"citations": 9, "h_index": 2, "i10_index": 0}\n'
            path.write_bytes(previous)
            sync.write_metrics(path, sync.parse_metrics(profile()), dry_run=True)
            self.assertEqual(path.read_bytes(), previous)
            with patch('sys.argv', ['sync', '--output', str(path)]), patch.object(sync, 'fetch_profile', return_value='blocked'):
                self.assertEqual(sync.main(), 1)
            self.assertEqual(path.read_bytes(), previous)

    def test_write_preserves_other_metadata_and_is_idempotent(self):
        with tempfile.TemporaryDirectory(prefix='.test-scholar-', dir=sync.ROOT) as directory:
            path = Path(directory) / 'metrics.json'
            path.write_text('{"note":"keep"}')
            metrics = sync.parse_metrics(profile())
            self.assertTrue(sync.write_metrics(path, metrics))
            self.assertEqual(json.loads(path.read_text())['note'], 'keep')
            self.assertFalse(sync.write_metrics(path, metrics))


if __name__ == '__main__':
    unittest.main()
