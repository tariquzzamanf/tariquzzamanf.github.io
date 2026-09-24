#!/usr/bin/env python3
"""Synchronize the public Google Scholar summary metrics for this site.

Google Scholar is not an API and may rate-limit automated requests.  This
script therefore updates only the small, curated metrics file and writes it
atomically after all three values have been parsed successfully.  Publication
metadata stays in content/publications.json because its author order, status,
topics, and resources are editorial records.

Usage:
    python3 scripts/sync_scholar.py
    python3 scripts/sync_scholar.py --dry-run
    python3 scripts/sync_scholar.py --user-id LWB_NzwAAAAJ
"""

from __future__ import annotations

import argparse
import datetime as dt
from html.parser import HTMLParser
import json
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_USER_ID = "LWB_NzwAAAAJ"
DEFAULT_OUTPUT = ROOT / "content" / "scholar-metrics.json"
SCHOLAR_URL = "https://scholar.google.com/citations?user={user_id}&hl=en"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def fetch_profile(user_id: str) -> str:
    """Fetch one public profile page, retrying transient HTTP failures."""
    request = urllib.request.Request(
        SCHOLAR_URL.format(user_id=user_id),
        headers={"User-Agent": USER_AGENT, "Accept-Language": "en"},
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", "replace")
            if "gsc_rsb_std" not in body:
                raise RuntimeError("the response did not contain Scholar metrics")
            return body
        except (urllib.error.URLError, TimeoutError, RuntimeError) as error:
            last_error = error
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Google Scholar request failed: {last_error}") from last_error


class MetricsTable(HTMLParser):
    """Collect cells only from the profile's summary table, including blanks."""

    def __init__(self):
        super().__init__()
        self.in_table = False
        self.rows = []
        self.row = []
        self.cell = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table" and attrs.get("id") == "gsc_rsb_st":
            self.in_table = True
        if self.in_table:
            if tag == "tr":
                self.row = []
            elif tag == "td":
                self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if self.in_table:
            if tag == "td" and self.cell is not None:
                self.row.append("".join(self.cell).strip())
                self.cell = None
            elif tag == "tr" and self.row:
                self.rows.append(self.row)
            elif tag == "table":
                self.in_table = False


def parse_metrics(page: str) -> dict[str, int]:
    """Use the labeled all-time column; reject incomplete or blocked pages."""
    parser = MetricsTable()
    parser.feed(page)
    labels = {"Citations": "citations", "h-index": "h_index", "i10-index": "i10_index"}
    metrics = {}
    for row in parser.rows:
        if row[0] not in labels:
            continue
        if len(row) != 3 or not re.fullmatch(r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)", row[1]):
            raise RuntimeError("Scholar returned an incomplete or invalid summary row")
        key = labels[row[0]]
        if key in metrics:
            raise RuntimeError("Scholar returned duplicate summary rows")
        metrics[key] = int(row[1].replace(",", ""))
    if set(metrics) != set(labels.values()):
        raise RuntimeError("Scholar summary is missing; the request may have been blocked")
    return metrics


def write_metrics(path: Path, metrics: dict[str, int], dry_run: bool = False) -> bool:
    """Merge fresh metrics into the existing JSON and atomically replace it."""
    existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    updated = {
        **existing,
        **metrics,
        "verified_on": dt.datetime.now(dt.timezone.utc).date().isoformat(),
        "source": "google-scholar",
    }
    changed = updated != existing
    if changed and not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
        ) as temporary:
            json.dump(updated, temporary, indent=2)
            temporary.write("\n")
            temporary_path = Path(temporary.name)
        temporary_path.replace(path)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user-id", default=DEFAULT_USER_ID, help="Google Scholar profile ID")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help=argparse.SUPPRESS)
    parser.add_argument("--dry-run", action="store_true", help="print values without writing JSON")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.user_id):
        parser.error("invalid Scholar profile ID")

    try:
        metrics = parse_metrics(fetch_profile(args.user_id))
        changed = write_metrics(args.output, metrics, dry_run=args.dry_run)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Scholar sync skipped: {error}", file=sys.stderr)
        return 1

    action = "would update" if args.dry_run else ("updated" if changed else "already current")
    print(
        f"Scholar metrics {action}: citations={metrics['citations']}, "
        f"h-index={metrics['h_index']}, i10-index={metrics['i10_index']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
