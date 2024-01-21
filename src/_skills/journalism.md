---
title: Journalism skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

We value community, and the life stories within. To capture and share these stories appropriately, we started developing a skill set of journalism.

<ul id="journalism">
{% for item in skills %}
{% if item.Category == 'Journalism' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
