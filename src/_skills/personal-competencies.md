---
title: Personal competencies
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

In general, we became more confident, more productive, happier people. As the project grows, we grow too.

<ul id="personal">
{% for item in skills %}
{% if item.Category == 'Personal competencies' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
