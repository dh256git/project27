---
layout: default
title: Volunteering
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-10-02
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamCC = site.volunteering | where:"team","CC" %}

### Leadership team - the C-suite

Join the management team.
There are {{ teamLeadership | size }} available tasks.
Members of the C-suite lead by example, and help with the management of {{ site.brand }}. We need to plan the future, while coordinating our work in the present.

{% for member in teamLeadership %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}
