---
year: '{{date.format("YYYY")}}'
aliases:
  - "{{shortTitle}}"
  - "{% if not shortTitle %} {{title}} {% endif %}"
journal: "{{publicationTitle}}"
authors:
{% for creator in creators %}
	{%- if creator.name -%}
		- "[[{{creator.name}}]]"
	{%- else -%}
		- "[[{{creator.firstName}} {{creator.lastName}}]]"
	{%- endif %}
{% endfor -%}

---
# {{title}}
{{bibliography}}

{% if abstractNote %}
### Abstract
{{abstractNote}}
{% endif %}

CiteKey: {{citationKey}}
{% if DOI %}
DOI: [{{DOI}}]({{DOI}})
{% endif %}
{% if url %}
URL: [{{url}}]({{url}})
{% endif %}
[Zotero Link]({{select}})

