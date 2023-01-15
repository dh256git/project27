---
layout: default
title: Volunteering
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2020-10-02
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamCC = site.volunteering | where:"team","CC" %}

### Editorial and review team

Join the Editorial and Review team.
There are {{ teamER | size }} available tasks.
The team of editors and reviewers help us make sure content is relevant and a high quality.

{% for member in teamER %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}
