---
title: Entrepreneurship skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

Entrepreneurship enables us to evaluate the viability of working on {{ site.brand }} as a social enterprise. It is the entrepreneurial skills that transform our hobby behind closed doors into a safe-space for all to participate in learning. 

<ul id="entrepreneurship">
{% for item in skills %}
{% if item.Category == 'Entrepreneurship' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
