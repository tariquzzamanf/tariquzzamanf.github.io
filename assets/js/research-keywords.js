(function (global) {
    'use strict';

    var palette = [
        '#e74c3c',
        '#9b59b6',
        '#f1c40f',
        '#3498db',
        '#2ecc71',
        '#1abc9c',
        '#e67e22',
        '#e84393',
        '#34495e',
        '#00a8cc',
        '#8e6e53',
        '#6c5ce7',
        '#c0392b',
        '#16a085',
        '#d35400',
        '#2c3e50'
    ];

    function createRegistry(keywordGroups) {
        var labels = [];
        var colors = Object.create(null);
        var indexes = Object.create(null);

        keywordGroups.forEach(function (keywords) {
            (keywords || []).forEach(function (rawKeyword) {
                var keyword = String(rawKeyword).trim();

                if (!keyword || Object.prototype.hasOwnProperty.call(colors, keyword)) {
                    return;
                }

                indexes[keyword] = labels.length;
                colors[keyword] = palette[labels.length % palette.length];
                labels.push(keyword);
            });
        });

        return {
            labels: labels,
            colorFor: function (keyword) {
                return colors[String(keyword || '').trim()] || '#7f8c8d';
            },
            indexFor: function (keyword) {
                var normalizedKeyword = String(keyword || '').trim();
                return Object.prototype.hasOwnProperty.call(indexes, normalizedKeyword)
                    ? indexes[normalizedKeyword]
                    : -1;
            }
        };
    }

    global.ResearchKeywords = {
        createRegistry: createRegistry
    };
})(window);
