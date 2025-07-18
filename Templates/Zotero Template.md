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
DOI: [{{DOI}}]({{DOI}})
[Zotero Link]({{select}})

