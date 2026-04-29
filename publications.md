---
layout: page
title: "Publications"
permalink: /publications/
---

<style>
  .pub-section { margin: 2em 0 2.5em; }
  .pub-section h2 {
    display: flex;
    align-items: baseline;
    gap: 0.6em;
    font-size: 1.35em;
    margin: 0 0 0.8em 0;
    padding-bottom: 0.35em;
    border-bottom: 2px solid #eee;
  }
  .pub-count {
    font-size: 0.7em;
    color: #888;
    font-weight: 400;
  }
  .pub-list { list-style: none; padding: 0; margin: 0; }
  .pub-item {
    padding: 1em 0;
    border-bottom: 1px solid #f0f0f0;
    line-height: 1.55;
  }
  .pub-item:last-child { border-bottom: none; }
  .pub-title { font-weight: 600; color: #222; display: block; margin-bottom: 0.2em; }
  .pub-authors { color: #444; font-size: 0.95em; }
  .pub-authors strong { color: #111; }
  .pub-meta {
    color: #666;
    font-size: 0.9em;
    font-style: italic;
    margin-top: 0.15em;
  }
  .pub-venue { font-style: italic; }
  .pub-links { font-size: 0.85em; margin-top: 0.3em; }
  .pub-links a {
    display: inline-block;
    margin-right: 0.8em;
    color: #2a6dad;
    text-decoration: none;
    border-bottom: 1px dotted #2a6dad;
  }
  .pub-links a:hover { color: #c9a227; border-bottom-color: #c9a227; }
  .pub-notes {
    color: #888;
    font-size: 0.85em;
    margin-top: 0.2em;
  }
  .pub-empty { color: #aaa; font-style: italic; padding: 0.5em 0; }

  .status-badge {
    display: inline-block;
    padding: 0.18em 0.7em;
    border-radius: 999px;
    font-size: 0.7em;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    vertical-align: middle;
  }
  .status-published    { background: #e6f4ea; color: #1e6b34; }
  .status-in_press     { background: #fff4d6; color: #8a6500; }
  .status-under_review { background: #e3edff; color: #1a4a9c; }
  .status-submitted    { background: #f1e8ff; color: #5b2c91; }
  .status-in_preparation { background: #efefef; color: #555; }
</style>

A current list of my research output. Source data lives in [`_data/publications.yml`](https://github.com/cjqu001/cjqu001.github.io/blob/main/_data/publications.yml) — edit that single file to add or update entries.

{%- assign status_order = "published,in_press,under_review,submitted,in_preparation" | split: "," -%}
{%- assign labels = "Published,In Press,Under Review,Submitted,In Preparation" | split: "," -%}

{%- for status in status_order -%}
  {%- assign label = labels[forloop.index0] -%}
  {%- assign group = site.data.publications | where: "status", status | sort: "year" | reverse -%}

  <div class="pub-section">
    <h2>
      <span>{{ label }}</span>
      <span class="status-badge status-{{ status }}">{{ label }}</span>
      <span class="pub-count">{{ group | size }}</span>
    </h2>

    {% if group.size == 0 %}
      <p class="pub-empty">None yet.</p>
    {% else %}
      <ul class="pub-list">
        {%- for pub in group -%}
          <li class="pub-item">
            <span class="pub-title">{{ pub.title }}</span>
            <span class="pub-authors">
              {%- assign authors = pub.authors | default: "" -%}
              {%- if pub.bold_self != false and authors contains "Quinones CJ" -%}
                {{ authors | replace: "Quinones CJ", "<strong>Quinones CJ</strong>" }}
              {%- else -%}
                {{ authors }}
              {%- endif -%}
            </span>
            <div class="pub-meta">
              {%- if pub.venue %}<span class="pub-venue">{{ pub.venue }}</span>{% endif -%}
              {%- if pub.venue and pub.year %}, {% endif -%}
              {%- if pub.year %}{{ pub.year }}{% endif -%}
            </div>
            {%- if pub.doi or pub.url or pub.pmid -%}
              <div class="pub-links">
                {%- if pub.doi %}<a href="https://doi.org/{{ pub.doi }}" target="_blank" rel="noopener">DOI: {{ pub.doi }}</a>{% endif -%}
                {%- if pub.url %}<a href="{{ pub.url }}" target="_blank" rel="noopener">Link</a>{% endif -%}
                {%- if pub.pmid %}<a href="https://pubmed.ncbi.nlm.nih.gov/{{ pub.pmid }}/" target="_blank" rel="noopener">PMID: {{ pub.pmid }}</a>{% endif -%}
              </div>
            {%- endif -%}
            {%- if pub.notes -%}
              <div class="pub-notes">{{ pub.notes }}</div>
            {%- endif -%}
          </li>
        {%- endfor -%}
      </ul>
    {% endif %}
  </div>
{%- endfor -%}

---

### Adding a publication

1. Open [`_data/publications.yml`](https://github.com/cjqu001/cjqu001.github.io/blob/main/_data/publications.yml).
2. Copy an existing entry, paste at the bottom, edit fields.
3. Set `status:` to one of `published`, `in_press`, `under_review`, `submitted`, `in_preparation`.
4. Commit. The page updates automatically on next build.
