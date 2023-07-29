---
title: Content
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2020-10-02
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamContent = site.volunteering | where:"team","Content" %}

### The Posts and Notes team

Join the Posts and Notes (P&N) team.
The P&N team helps with authoring new posts for our blog, and new notes for the {{ site.brand }} {{ site.product }}.

### Activity list

{% assign taskCountContent = teamContent | size %}
{% case taskCountContent %}
{% when 1 %}There is {{ taskCountContent }} available activity.
{% else %}There are {{ taskCountContent }} available activities.
{% endcase %}

{% for member in teamContent %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a target="_blank" rel="noreferrer noopener" href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">{{ member.task }}: View tasks and the activity description</a>
{% else %}
<p>Currently no activities are available in this team.</p>
{% endfor %}