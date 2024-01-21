---
title: Research skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

True to our origins from university life, we continue to develop our research skills, let it be academic, user, or market research.

<ul id="research">
{% for item in skills %}
{% if item.Category == 'Research' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
