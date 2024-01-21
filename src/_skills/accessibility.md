---
layout: default
title: Accessibility skillset
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

The accessibility skill set is useful to anyone, who wants to learn how to make web content accessible to screen reader users, as well as learning disabled and low vision visitors. We strive to develop the best user experience, making our space disability inclusive.

### Skills to develop

<ul id="accessibility-skills">
{% for item in skills %}
{% if item.Category == 'Accessibility' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Web development

Web development is a very valuable skill set in the 2020s. Knowing how to develop a web space, enabled us to make {{ site.brand }} available on multiple devices, such as your smart phone or desktop computer. 

<ul id="web-dev-skills">
{% for item in skills %}
{% if item.Category == 'Web development' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>
