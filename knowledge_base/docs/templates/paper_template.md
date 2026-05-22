# {{ title }}

<section class="paper-meta-grid" aria-label="Paper metadata">
{% if authors %}
  <div class="paper-meta-card paper-meta-card--wide">
    <div class="paper-meta-card__label">Authors</div>
    <div class="paper-meta-card__value paper-meta-authors">
{% for author in authors %}
      <a href="../../tag-search/?author={{ author | url_quote }}">{{ author | e }}</a>{% if not loop.last %}<span>, </span>{% endif %}
{% endfor %}
    </div>
  </div>
{% endif %}
{% if year %}
  <div class="paper-meta-card">
    <div class="paper-meta-card__label">Year</div>
    <div class="paper-meta-card__value paper-meta-card__value--large">
      <a href="../../tag-search/?year={{ year | url_quote }}">{{ year | e }}</a>
    </div>
{% if type %}
    <div class="paper-meta-card__detail">{{ type | e }}</div>
{% endif %}
  </div>
{% endif %}
{% if algorithm %}
  <div class="paper-meta-card">
    <div class="paper-meta-card__label">Algorithm</div>
    <div class="paper-meta-card__value">{{ algorithm | e }}</div>
  </div>
{% endif %}
{% if source %}
  <div class="paper-meta-card">
    <div class="paper-meta-card__label">Source</div>
    <div class="paper-meta-card__value">{{ source | e }}</div>
  </div>
{% endif %}
{% if arxiv_clean or doi_clean %}
  <div class="paper-meta-card">
    <div class="paper-meta-card__label">Identifiers</div>
    <div class="paper-meta-card__value paper-meta-identifiers">
{% if arxiv_clean %}
      <a href="https://arxiv.org/abs/{{ arxiv_clean | url_path_quote }}" target="_blank" rel="noopener noreferrer">arXiv {{ arxiv_clean | e }}</a>
{% endif %}
{% if doi_clean %}
      <a href="https://doi.org/{{ doi_clean | url_path_quote }}" target="_blank" rel="noopener noreferrer">DOI {{ doi_clean | e }}</a>
{% endif %}
    </div>
  </div>
{% endif %}
</section>

## Abstract

{{ abstract | metadata_text_html }}

{% if summary %}
## Summary

{{ summary | metadata_text_html }}
{% endif %}

{% if link_sections %}
## Links

<div class="paper-link-stack">
{% for section in link_sections %}
  <section class="paper-link-section paper-link-section--{{ section.kind | e }}">
    <h3>{{ section.title | e }}</h3>
    <div class="paper-link-pills">
{% for item in section.links %}
      <a class="paper-link-pill paper-link-pill--{{ item.variant | e }}" href="{{ item.url | e }}"{% if item.external %} target="_blank" rel="noopener noreferrer"{% endif %}>
        <span class="paper-link-pill__label">{{ item.label | e }}</span>
      </a>
{% endfor %}
    </div>
  </section>
{% endfor %}
</div>
{% endif %}

{% if tags %}
## Tags

<div class="paper-tag-list">
{% for tag in tag_links %}
  <a class="paper-tag-chip" href="{{ tag.url | e }}">{{ tag.label | e }}</a>
{% endfor %}
</div>
{% endif %}

{% if top_similar_papers %}
## Top 5 Most Similar Papers

<div class="paper-similar-list">
{% for paper in top_similar_papers %}
  <article class="paper-similar-card">
    <div class="paper-similar-card__rank">{{ loop.index }}</div>
    <div class="paper-similar-card__body">
      <div class="paper-similar-card__meta">
{% if paper.byline %}
        <span>{{ paper.byline | e }}</span>
{% endif %}
        <span>{{ paper.score_label | e }}</span>
      </div>
      <h3><a href="{{ paper.url | e }}">{{ paper.title | e }}</a></h3>
{% if paper.label and paper.label != paper.title %}
      <p class="paper-similar-card__label">{{ paper.label | e }}</p>
{% endif %}
{% if paper.summary %}
      <p class="paper-similar-card__summary">{{ paper.summary | e }}</p>
{% endif %}
      <div class="paper-link-pills paper-similar-card__actions">
        <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.url | e }}"><span class="paper-link-pill__label">Open Detail Page</span></a>
        <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.map_url | e }}"><span class="paper-link-pill__label">Open in Map</span></a>
        <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.tree_url | e }}"><span class="paper-link-pill__label">Open in Tree</span></a>
      </div>
    </div>
  </article>
{% endfor %}
</div>
{% endif %}
