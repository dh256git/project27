---
title: Digital skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

Web development is an essential skill set that matters to us; however, we also needed to learn additional digital skills to be able to build and manage {{ site.brand }}.

<ul id="digital-skills">
{% for item in skills %}
{% if item.Category == 'Digital skills' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
