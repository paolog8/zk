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
citeKey: "{{citationKey}}"
{% if DOI %}
DOI: {{DOI}}
{% endif %}
{% if url %}
URL: {{url}}
{% endif %}
---
# {{title}}
{{bibliography}}

[Zotero Link]({{select}})

{% if abstractNote %}
### Abstract
{{abstractNote}}
{% endif %}

%%{% persist "notes" %} {% if notes%}
 ### Notes
{% for noteItem in notes %}
{{noteItem.note}}
{% endfor %}
{% endif %}
{% endpersist %} %%