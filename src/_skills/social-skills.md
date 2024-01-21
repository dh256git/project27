---
title: Social skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

No doubt, we have picked up many technical skills on the way, but in the process we also strengthened our social skills.

<ul id="social-skills">
{% for item in skills %}
{% if item.Category == 'Social skills' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
