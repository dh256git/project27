---
layout: default
title: Training
levelToOpen: workspace on Trello
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
listOfIcons: [["fas fa-list-check", ""], ["fas fa-people-group", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
---

{% assign volumeInfo = site.data.volumes.guide[5] %}
{% assign dataFile = site.data.chapters.training %}

## {{ volumeInfo.name }}

{{ volumeInfo.description }}

{% include global/grid-generator.html heading="h3" %}