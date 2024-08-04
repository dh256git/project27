---
layout: solutions
title: Projects
tagline: From academic projects to scalable solutions
pitch: Browse a list of research and innovation projects we collaborated on.
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2023-06-24
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
burndownData: /solutions/projects/current-sprint.csv
---

## Research and innovation portfolio

All of the solutions in our portfolio have been [co-designed with researchers,]({% link solutions/research-services/index.md %}) and the projects are grounded in peer reviewed science.
To maximise impact, we are working with businesses on [diffusing innovation that works.]({% link solutions/innovation-services/index.md %})

{% assign dataFile = site.data.solutions.projects %}
{% assign gridLimit = 2 %}
{% include global/grid-generator-for-solutions.html heading="h3" %}

## Community portfolio

All of our community projects are inspired by the skills our community members want to develop.

{% assign dataFile = site.data.solutions.projects %}
{% assign gridOffset = 2 %}
{% include global/grid-generator-for-solutions.html heading="h3" %}

---

## Project spotlight

Learn more about Olli, by viewing curated content in the tabs below.
<div class="container-mt-5">
{% include projects/solutions/tabs-for-projects.html %}
</div>