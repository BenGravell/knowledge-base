# {{ title }}

**Authors**: {{ authors | join(", ") }}

**Published**: {{ year }} ({{ type }})

{% if source %}
**Source**: {{ source }}
{% endif %}

{% if algorithm %}
**Algorithm**: {{ algorithm }}
{% endif %}

## Summary

{{ summary }}

{% if link %}
## Links

- [Paper]({{ link }})
{% endif %}

{% if links_alt %}
### Additional Links

{% for link in links_alt %}
- [{{ link }}]({{ link }})
{% endfor %}
{% endif %}

{% if tags %}
## Tags

{% for tag in tags %}
- {{ tag }}
{% endfor %}
{% endif %}
