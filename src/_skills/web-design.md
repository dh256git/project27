---
layout: default
title: Web design skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

Web development is a very valuable skill set in the 2020s. Knowing how to develop a web space, enabled us to make {{ site.brand }} available on multiple devices, such as your smart phone or desktop computer. 

### Skills to develop

<ul id="web-dev-skills">
{% for item in skills %}
{% if item.Category == 'Web development' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
