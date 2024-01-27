---
layout: default
title: Community Projects
levelToOpen: project
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
listOfIcons: [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
---
{% assign volumeInfo = site.data.volumes.guide[6] %}
{% assign dataFile = site.data.chapters.projects %}

## {{ volumeInfo.name }}

{{ volumeInfo.description }}

{% include global/grid-generator.html heading="h3" %}