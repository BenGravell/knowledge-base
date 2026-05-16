# {{ title }}

**Authors**: {{ authors | join(", ") }}

**Published**: {{ year }} ({{ type }})

{% if source %}
**Source**: {{ source }}
{% endif %}

{% if algorithm %}
**Algorithm**: {{ algorithm }}
{% endif %}

{% if arxiv_id %}
**arXiv**: {{ arxiv_id }}
{% endif %}

{% if doi %}
**DOI**: {{ doi }}
{% endif %}

## Summary

{{ summary | metadata_text_html }}

## Abstract

{{ abstract | metadata_text_html }}

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
{% if item.detail %}
        <span class="paper-link-pill__detail">{{ item.detail | e }}</span>
{% endif %}
      </a>
{% endfor %}
    </div>
  </section>
{% endfor %}
</div>
{% endif %}

{% if tags %}
## Tags

{% for tag in tags %}
- {{ tag }}
{% endfor %}
{% endif %}
