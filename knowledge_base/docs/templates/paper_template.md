# {{ title }} {.paper-detail-title}

<section class="paper-meta-grid" aria-label="Paper metadata">
{% if authors %}
  <div class="paper-meta-card paper-meta-card--wide">
    <div class="paper-meta-card__label">Authors</div>
    <div class="paper-meta-card__value paper-meta-authors">
{% for author in authors %}
      <a href="../../search/?author={{ author | url_quote }}">{{ author | e }}</a>{% if not loop.last %}<span>, </span>{% endif %}
{% endfor %}
    </div>
  </div>
{% endif %}
{% if year %}
  <div class="paper-meta-card">
    <div class="paper-meta-card__label">Year</div>
    <div class="paper-meta-card__value paper-meta-card__value--large">
      <a href="../../search/?year={{ year | url_quote }}">{{ year | e }}</a>
    </div>
{% if type %}
    <div class="paper-meta-card__detail"><a href="../../search/?type={{ type | url_quote }}">{{ type | e }}</a></div>
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
    <div class="paper-meta-card__value"><a href="../../search/?source={{ source | url_quote }}">{{ source | e }}</a></div>
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
      <a class="paper-link-pill paper-link-pill--{{ item.variant | e }}" href="{{ item.url | e }}"{% if item.detail %} aria-label="{{ item.detail | e }}" title="{{ item.detail | e }}"{% endif %}{% if item.external %} target="_blank" rel="noopener noreferrer"{% endif %}>
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
    <div class="paper-similar-card__rank" style="--paper-similar-gauge: {{ paper.score_gauge_degrees }}deg;" aria-label="{{ paper.score_label | e }}">
      <div class="paper-similar-card__rank-top">{{ loop.index }}</div>
      <div class="paper-similar-card__rank-bottom">
        <span>{{ paper.score_percent | e }}%</span>
      </div>
    </div>
    <div class="paper-similar-card__body">
      <h3><a href="{{ paper.url | e }}">{{ paper.title | e }}</a></h3>
{% if paper.label and paper.label != paper.title %}
      <p class="paper-similar-card__label">{{ paper.label | e }}</p>
{% endif %}
{% if paper.byline %}
      <div class="paper-similar-card__meta">
        <span>{{ paper.byline | e }}</span>
      </div>
{% endif %}
      <div class="paper-similar-card__actions">
        <div class="paper-similar-card__action-row">
          <div class="paper-link-pills paper-similar-card__action-links">
            <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.url | e }}"><span class="paper-link-pill__label">Detail</span></a>
            <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.map_url | e }}"><span class="paper-link-pill__label">Map</span></a>
            <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.tree_url | e }}"><span class="paper-link-pill__label">Tree</span></a>
            <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.timeline_url | e }}"><span class="paper-link-pill__label">Timeline</span></a>
            <a class="paper-link-pill paper-link-pill--internal" href="{{ paper.search_url | e }}"><span class="paper-link-pill__label">Search</span></a>
          </div>
        </div>
      </div>
    </div>
  </article>
{% endfor %}
</div>
{% endif %}
