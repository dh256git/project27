---
layout: default
title: Research & Development
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

### Research and Development team

Join the Research and Development (R&D) team.
There are {{ teamRnD | size }} available tasks.
The R&D team members help with the research and development activities of {{ site.brand }}, such as website development or researching solutions to ongoing challenges in the project.

{% for member in teamRnD %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}
