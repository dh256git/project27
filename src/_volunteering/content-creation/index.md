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

### Content Creation team

Join the Content Creation team.
There are {{ teamCC | size }} available tasks.
The Content Creation team helps with authoring new notes for {{ site.product }}.

{% for member in teamCC %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}
