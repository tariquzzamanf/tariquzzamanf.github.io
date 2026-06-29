---
permalink: /
title: "Md. Tariquzzaman"
description: "Md. Tariquzzaman is a Junior Lecturer in CSE at Islamic University of Technology (IUT), researching natural language processing, Bangla NLP, misinformation detection, sign language instruction generation, and LLM evaluation."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
        .transparent-button {
            display: inline-block;
            background-color: transparent;
            border: 1px solid #3498db;
            color: #3498db;
            padding: 6px 14px;
            margin-top: 6px; /* add breathing room above buttons */
            font-size: 12px;
            font-weight: 500;
            cursor: pointer;
            border-radius: 999px;
            text-decoration: none;
            line-height: 1.4;
            transition:
                background-color 0.2s ease,
                color 0.2s ease,
                box-shadow 0.2s ease,
                transform 0.2s ease,
                border-color 0.2s ease;
        }

        .transparent-button:hover {
            background-color: #3498db;
            color: #ffffff;
            border-color: #3498db;
            box-shadow: 0 4px 10px rgba(52, 152, 219, 0.4);
            transform: translateY(-1px);
        }

        .justified-text {
            text-align: justify;
        }

        .justified-text a,
        .justified-text a:visited {
            color: #000;
            text-decoration: underline;
        }

        .justified-text-para {
            text-align: justify;
            font-size: 16px;
        }

        .news-container {
            max-height: 180px;
            overflow-y: auto;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 12px 24px 12px 36px; /* extra left padding for bullets */
            margin-bottom: 40px;
            scrollbar-width: thin;
            scrollbar-color: #888 #f0f0f0;
        }

        .news-container::-webkit-scrollbar {
            width: 8px;
        }

        .news-container::-webkit-scrollbar-track {
            background: #f0f0f0;
            border-radius: 4px;
        }

        .news-container::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }

        .news-container::-webkit-scrollbar-thumb:hover {
            background: #666;
        }

        .news-item {
            padding: 6px 0;
            border-bottom: 1px solid #f0f0f0;
        }

        .news-item:last-child {
            border-bottom: none;
        }

        /* ── Research Map ── */
        #research-map-section {
            margin-bottom: 28px;
        }

        #research-map {
            position: relative;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            background: linear-gradient(135deg, #fafbfc 0%, #f5f6f8 100%);
            overflow: hidden;
            aspect-ratio: 4 / 3;
            width: 66.66%;
            margin: 0 auto;
        }

        #research-map svg {
            display: block;
            width: 100%;
            height: 100%;
        }

        .rm-node {
            cursor: pointer;
        }

        .rm-node circle {
            transition: filter 0.15s, stroke-width 0.15s;
        }

        .rm-node:hover circle {
            filter: brightness(1.12) drop-shadow(0 0 5px rgba(0,0,0,0.2));
        }

        .rm-node-active circle {
            stroke: #333;
            stroke-width: 3px;
            filter: drop-shadow(0 0 6px rgba(0,0,0,0.25));
        }

        .rm-node text {
            pointer-events: none;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 10px;
            font-weight: 700;
            fill: #fff;
            text-anchor: middle;
            dominant-baseline: central;
            user-select: none;
        }

        .rm-edge {
            stroke: #d0d0d0;
            stroke-width: 1.5;
            stroke-opacity: 0.5;
            transition: stroke 0.15s, stroke-opacity 0.15s;
        }

        .rm-edge-active {
            stroke: #888 !important;
            stroke-width: 2.5 !important;
            stroke-opacity: 1 !important;
        }

        .rm-tooltip {
            position: absolute;
            background: #fff;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 16px 20px 14px;
            box-shadow: 0 6px 24px rgba(0,0,0,0.13);
            max-width: 320px;
            min-width: 200px;
            z-index: 10;
            font-size: 0.88em;
            line-height: 1.55;
            animation: rmFadeIn 0.15s ease;
        }

        @keyframes rmFadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .rm-tooltip-title {
            font-weight: 700;
            margin-bottom: 2px;
            color: #222;
            font-size: 0.95em;
            padding-right: 22px;
        }

        .rm-tooltip-venue {
            font-size: 0.8em;
            color: #999;
            margin-bottom: 8px;
        }

        .rm-tooltip-tldr {
            color: #555;
            font-size: 0.9em;
        }

        .rm-tooltip-keywords {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 9px;
        }

        .rm-tooltip-keyword {
            padding: 2px 7px;
            border: 1px solid currentColor;
            border-radius: 999px;
            background: #fff;
            font-size: 0.72em;
            font-weight: 600;
            line-height: 1.3;
        }

        .rm-tooltip-close {
            position: absolute;
            top: 10px;
            right: 14px;
            cursor: pointer;
            font-size: 16px;
            color: #bbb;
            background: none;
            border: none;
            padding: 0;
            line-height: 1;
        }

        .rm-tooltip-close:hover {
            color: #333;
        }

        .rm-legend {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-top: 10px;
            padding: 0 2px;
        }

        .rm-legend-item {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 0.72em;
            color: #777;
        }

        .rm-legend-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
            flex-shrink: 0;
        }

        .research-highlight-image {
            display: block;
            width: var(--highlight-image-width, 100%);
            max-width: 100%;
            height: auto;
            margin: 16px auto;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
        }

        @media screen and (max-width: 600px) {
            .rm-tooltip {
                max-width: 240px;
                min-width: 160px;
                font-size: 0.82em;
            }

            .research-highlight-image {
                width: 100%;
            }
        }
    </style>

<p class="justified-text">
Hi, I'm Md. Tariquzzaman (Tariq), a <a href="https://cse.iutoic-dhaka.edu/profile/tariquzzaman/education" target="_blank" rel="noopener">Junior Lecturer</a> in the Department of Computer Science and Engineering (CSE) at the <a href="https://www.iutoic-dhaka.edu/" target="_blank" rel="noopener">Islamic University of Technology (IUT)</a>. I am an active member of the <a href="https://cse.iutoic-dhaka.edu/ssl" target="_blank" rel="noopener">Systems and Software Lab (SSL)</a> research group at IUT. I worked on my undergraduate thesis under the supervision of <a href="https://cse.iutoic-dhaka.edu/profile/mohsinul/education" target="_blank" rel="noopener">Mohsinul Kabir</a>, and I am pursuing my graduate studies under the supervision of <a href="https://cse.iutoic-dhaka.edu/profile/hasan/education" target="_blank" rel="noopener">Hasan Mahmud</a>.
</p>

<p class="justified-text">
My research interests lie broadly in Natural Language Processing. I am working on projects related to low-resource language processing for Bangla language, harmful content and misinformation detection, sign language instruction generation, and benchmarking scenario-induced biases in large language models.
</p>
<h2>News and Updates</h2>
<ul class="news-container">
  <li class="news-item"><strong>Mar 2026:</strong> Paper <em><a href="https://arxiv.org/abs/2601.05403" target="_blank" rel="noopener">"Same Claim, Different Judgment: Benchmarking Scenario-Induced Bias in Multilingual Financial Misinformation Detection"</a></em> accepted to Findings of ACL 2026.</li>
  <li class="news-item"><strong>Oct 2025:</strong> Paper <em><a href="https://openreview.net/forum?id=KkVMBkjbra" target="_blank" rel="noopener">"Prompting with Sign Parameters for Low-resource Sign Language Instruction Generation"</a></em> accepted at CV4A11y workshop at ICCV 2025.</li>
  <li class="news-item"><strong>Dec 2024:</strong> Paper <em><a href="https://arxiv.org/abs/2412.08753" target="_blank" rel="noopener">"BDA: Bangla Text Data Augmentation Framework"</a></em> submitted to arXiv.</li>
  <li class="news-item"><strong>Dec 2023:</strong> Paper <em><a href="https://aclanthology.org/2023.banglalp-1.26/" target="_blank" rel="noopener">"A Novel Informal Bangla FastText Embedding for Violence Inciting Text Detection"</a></em> received Best Shared Task Paper Award at BLP@EMNLP 2023.</li>
</ul>

<div id="research-map-section">
  <h2 style="margin-top:0; margin-bottom:16px; padding-bottom:8px; border-bottom:2px solid #e0e0e0;">Research Map</h2>
  <p style="font-size:0.85em; color:#999; margin-top:-10px; margin-bottom:12px;">
    The research map will help you navigate through my research portfolio. Click any node for details.
  </p>
  <div id="research-map"></div>
  <div class="rm-legend" id="rm-legend"></div>
</div>

<h2>Research Highlights</h2>
{% assign all_research_papers = "" | split: "" %}
{% for topic in site.data.research.topics %}
{% if topic.papers %}
{% assign all_research_papers = all_research_papers | concat: topic.papers %}
{% endif %}
{% endfor %}
{% assign highlighted_papers = all_research_papers | where: "ishighlight", 1 | sort: "year" | reverse %}
{% for paper in highlighted_papers %}
<h3>{{ paper.title }}</h3>
{% if paper.links %}
<p>{% for link in paper.links %}<a class="transparent-button" href="{{ link.url }}" target="_blank" rel="noopener">{{ link.label }}</a> {% endfor %}</p>
{% endif %}
{% if paper.image %}
<img class="research-highlight-image" src="{{ paper.image | relative_url }}" alt="{{ paper.image_alt }}" loading="lazy" style="--highlight-image-width: {{ paper.highlight_image_width | default: 100 }}%;">
{% else %}
<div style="height: 240px; margin: 16px 0; border: 1px dashed #ccc; border-radius: 6px; background: linear-gradient(135deg, #f5f6f7 0%, #eaecee 100%); display: flex; align-items: center; justify-content: center; color: #999;">Placeholder image</div>
{% endif %}
<p><strong>tldr.</strong> {{ paper.tldr }}</p>
{% endfor %}

<script src="{{ '/assets/js/research-keywords.js' | relative_url }}"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
(function () {
    var nodes = [
        {% for topic in site.data.research.topics %}
          {% for paper in topic.papers %}
            {
                id: {{ paper.id | jsonify }},
                nodename: {{ paper.nodename | jsonify }},
                full: {{ paper.title | jsonify }},
                tldr: {{ paper.tldr | default: paper.summary | default: '' | jsonify }},
                keywords: {{ paper.keywords | default: empty | jsonify }},
                venue: {{ paper.venue | default: '' | jsonify }},
                link: {{ '/research/#paper-' | append: paper.id | relative_url | jsonify }}
            },
          {% endfor %}
        {% endfor %}
    ];

    var keywordRegistry = window.ResearchKeywords.createRegistry(
        nodes.map(function(node) { return node.keywords; })
    );

    nodes.forEach(function(node) {
        node.primaryKeyword = node.keywords.length > 0 ? node.keywords[0] : '';
        node.keywordIndex = keywordRegistry.indexFor(node.primaryKeyword);
    });

    var links = [];
    for (var sourceIndex = 0; sourceIndex < nodes.length; sourceIndex += 1) {
        for (var targetIndex = sourceIndex + 1; targetIndex < nodes.length; targetIndex += 1) {
            var sharedKeywords = nodes[sourceIndex].keywords.filter(function(keyword) {
                return nodes[targetIndex].keywords.indexOf(keyword) !== -1;
            });

            if (sharedKeywords.length > 0) {
                links.push({
                    source: nodes[sourceIndex].id,
                    target: nodes[targetIndex].id,
                    sharedKeywords: sharedKeywords
                });
            }
        }
    }

    var container = document.getElementById('research-map');
    if (!container) return;
    var W = 800;
    var H = 600;

    var svg = d3.select('#research-map')
        .append('svg')
        .attr('viewBox', '0 0 ' + W + ' ' + H)
        .attr('preserveAspectRatio', 'xMidYMid meet')
        .style('width', '100%')
        .style('height', '100%')
        .style('cursor', 'grab');

    var defs = svg.append('defs');
    keywordRegistry.labels.forEach(function(keyword, index) {
        var color = keywordRegistry.colorFor(keyword);
        var grad = defs.append('radialGradient')
            .attr('id', 'grad-keyword-' + index);
        grad.append('stop').attr('offset', '0%').attr('stop-color', d3.color(color).brighter(0.4));
        grad.append('stop').attr('offset', '100%').attr('stop-color', color);
    });


    var simulation = d3.forceSimulation(nodes)
        .force('link', d3.forceLink(links).id(function(d) { return d.id; }).distance(90))
        .force('charge', d3.forceManyBody().strength(-260))
        .force('center', d3.forceCenter(W / 2, H / 2))
        .force('collision', d3.forceCollide().radius(30))
        .force('x', d3.forceX(W / 2).strength(0.06))
        .force('y', d3.forceY(H / 2).strength(0.06));

    var zoomGroup = svg.append('g');
    var linkGroup = zoomGroup.append('g');
    var nodeGroup = zoomGroup.append('g');

    var zoom = d3.zoom()
        .scaleExtent([0.3, 4])
        .filter(function(event) { return event.type !== 'wheel'; })
        .on('zoom', function(event) {
            zoomGroup.attr('transform', event.transform);
            svg.style('cursor', event.sourceEvent && event.sourceEvent.type === 'mousemove' ? 'grabbing' : 'grab');
        });

    svg.call(zoom);

    var initialScale = 1.4;
    var initialTransform = d3.zoomIdentity
        .translate(W / 2 * (1 - initialScale), H / 2 * (1 - initialScale))
        .scale(initialScale);
    svg.call(zoom.transform, initialTransform);

    var controls = d3.select('#research-map')
        .append('div')
        .style('position', 'absolute')
        .style('top', '10px')
        .style('right', '10px')
        .style('display', 'flex')
        .style('flex-direction', 'column')
        .style('gap', '4px')
        .style('z-index', '5');

    var btnStyle = 'width:26px;height:26px;border:1px solid #ddd;border-radius:5px;background:#fff;cursor:pointer;font-size:15px;line-height:1;color:#555;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);';

    controls.append('button').attr('style', btnStyle).text('+')
        .on('click', function() { svg.transition().duration(250).call(zoom.scaleBy, 1.4); });
    controls.append('button').attr('style', btnStyle).text('−')
        .on('click', function() { svg.transition().duration(250).call(zoom.scaleBy, 1 / 1.4); });
    controls.append('button').attr('style', btnStyle + 'font-size:10px;').text('⟳')
        .on('click', function() { svg.transition().duration(350).call(zoom.transform, initialTransform); });

    var link = linkGroup.selectAll('line')
        .data(links)
        .join('line')
        .attr('class', 'rm-edge');

    var node = nodeGroup.selectAll('g')
        .data(nodes)
        .join('g')
        .attr('class', 'rm-node')
        .call(d3.drag()
            .on('start', dragstarted)
            .on('drag', dragged)
            .on('end', dragended));

    node.append('circle')
        .attr('r', 24)
        .attr('fill', function(d) {
            return d.keywordIndex >= 0
                ? 'url(#grad-keyword-' + d.keywordIndex + ')'
                : '#7f8c8d';
        })
        .attr('stroke', '#fff')
        .attr('stroke-width', 2);

    node.append('text')
        .text(function(d) { return d.nodename; });

    node.on('click', function(event, d) {
        event.stopPropagation();

        node.classed('rm-node-active', false);
        link.classed('rm-edge-active', false);

        d3.select(this).classed('rm-node-active', true);
        link.classed('rm-edge-active', function(l) {
            return l.source.id === d.id || l.target.id === d.id;
        });

        showTooltip(d, event);
    });

    svg.on('click', function() {
        d3.select('.rm-tooltip').remove();
        node.classed('rm-node-active', false);
        link.classed('rm-edge-active', false);
    });

    function showTooltip(d, event) {
        d3.select('.rm-tooltip').remove();

        var rect = container.getBoundingClientRect();
        var x = event.clientX - rect.left + 14;
        var y = event.clientY - rect.top - 10;
        var cw = container.clientWidth;
        var ch = container.clientHeight;

        if (x + 330 > cw) x = x - 350;
        if (y + 140 > ch) y = y - 130;
        if (x < 8) x = 8;
        if (y < 8) y = 8;

        var topicDot = '<span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:'
            + keywordRegistry.colorFor(d.primaryKeyword) + ';margin-right:4px;vertical-align:middle;"></span>';

        var keywordHtml = d.keywords.map(function(keyword) {
            return '<span class="rm-tooltip-keyword" style="color:' + keywordRegistry.colorFor(keyword) + ';">'
                + escapeHtml(keyword) + '</span>';
        }).join('');

        var tooltip = d3.select('#research-map')
            .append('div')
            .attr('class', 'rm-tooltip')
            .style('left', x + 'px')
            .style('top', y + 'px');

        var linkIcon = d.link
            ? ' <a href="' + d.link + '" target="_blank" rel="noopener" onclick="event.stopPropagation();" title="Open paper" style="display:inline-flex;align-items:center;vertical-align:middle;margin-left:5px;color:#3498db;text-decoration:none;flex-shrink:0;">' +
              '<svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' +
              '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>' +
              '<polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></a>'
            : '';

        tooltip.html(
            '<button class="rm-tooltip-close" onclick="this.parentElement.remove();event.stopPropagation();">&times;</button>' +
            '<div class="rm-tooltip-title" style="display:flex;align-items:flex-start;gap:4px;">' +
            '<span>' + escapeHtml(d.full) + '</span>' + linkIcon + '</div>' +
            '<div class="rm-tooltip-venue">' + topicDot + escapeHtml(d.venue) + '</div>' +
            '<div class="rm-tooltip-tldr"><strong>TL;DR:</strong> ' + escapeHtml(d.tldr) + '</div>' +
            '<div class="rm-tooltip-keywords">' + keywordHtml + '</div>'
        );
    }

    function escapeHtml(value) {
        return String(value)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    simulation.on('tick', function() {
        link
            .attr('x1', function(d) { return d.source.x; })
            .attr('y1', function(d) { return d.source.y; })
            .attr('x2', function(d) { return d.target.x; })
            .attr('y2', function(d) { return d.target.y; });

        node.attr('transform', function(d) {
            return 'translate(' + d.x + ',' + d.y + ')';
        });
    });

    function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        svg.style('cursor', 'grabbing');
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }
    function dragged(event) {
        var t = d3.zoomTransform(svg.node());
        event.subject.fx = t.invertX(event.x);
        event.subject.fy = t.invertY(event.y);
    }
    function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        svg.style('cursor', 'grab');
        event.subject.fx = null;
        event.subject.fy = null;
    }

    var legendEl = document.getElementById('rm-legend');
    if (legendEl) {
        keywordRegistry.labels.forEach(function(keyword) {
            var item = document.createElement('span');
            item.className = 'rm-legend-item';
            item.innerHTML = '<span class="rm-legend-dot" style="background:'
                + keywordRegistry.colorFor(keyword) + '"></span>' + escapeHtml(keyword);
            legendEl.appendChild(item);
        });
    }
})();
</script>
