---
layout: default
title: Meet our allies
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-06-24
licence: copyright
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
pitch: Collaboration and partnership are ways in which we grow and make global impact.
---

{% assign collaborators = site.data.allies['Collaborators'] %}
{% assign funders = site.data.allies['Funders'] %}

### Collaborations and partnerships {#collaborations}

We collaborate with globally recognised research groups and partner with impactful social businesses to amplify our reach.

<div class="container mt-5">
<div class="row">
{% for item in collaborators %}
{% include global/profile-for-allies.html %}
{% endfor %}
</div>
</div>

### Funders {#funders}

Our work is made possible by a growing list of funders, who believe in the mission of {{ site.org }} and our collaborators.

<div class="container mt-5">
<div class="row">
{% for item in funders %}
{% include global/profile-for-allies.html %}
{% endfor %}
</div>
</div>