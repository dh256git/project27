---
layout: default
title: Guide
tagline: A journal of life-long learning
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-09-01
licence: copyright
buttonStyle: fg-guide-land
backgroundStyle: bg-guide-land
listOfIcons: [["fas fa-atom", ""], ["fas fa-desktop", ""], ["fas fa-chart-line"], ["fas fa-utensils", ""], ["fas fa-record-vinyl", ""], ["fas fa-graduation-cap", ""], ["fas fa-hands-holding-circle", ""]]
levelToOpen: volume
listOfDots: ["dots", "dots1", "dots2", "dots3", "dots4"]
listOfMore: ["more", "more1", "more2", "more3", "more4"]
listOfButtons: ["Read-more", "Read-more1", "Read-more2", "Read-more3", "Read-more4"]
listOfFunctions: ["readMoreMPS()", "readMoreComputerLiteracy()", "readMoreStatistics()", "readMoreCookbook()", "readMoreVocal()"]
tabpanelIDList: ["science", "lifestyle", "training"]
---

{% assign guide = site.data.main['Guide'] %}

## The {{ site.product }}: {{ page.tagline }}

The {{ site.brand }} {{ site.product }} is a collection of accessible notes for learning.
Our library has a science collection, and a lifestyle collection, organised into volumes.

Blind or learning disabled people can study our notes to learn about topics they are interested in.
Our volunteers and members can contribute to expanding the {{ site.product }}, and develop a wide range of skills on the way.

{% include global/cover-image.html image="guide-cover.jpg" alt="Someone is holding a paper map, and pointing at a location with a finger." %}

<div role='tablist'>
    <button role='tab' id='tab-science' aria-controls='tabpanel-science' onClick="setTab('science')">Science and Tech</button>
    <button role='tab' id='tab-lifestyle' aria-controls='tabpanel-lifestyle' onClick="setTab('lifestyle')">Lifestyle</button>
    <button role='tab' id='tab-training' aria-controls='tabpanel-training' onClick="setTab('training')">Training and community projects</button>
    </div>

{% for collection in guide %}
{% assign collectionIndex = forloop.index | minus: 1 %}
<div role='tabpanel' id='tabpanel-{{ page.tabpanelIDList[collectionIndex] }}' aria-labelledby='tab-{{ page.tabpanelIDList[collectionIndex] }}'>
{% capture collection-content %}
### {{ collection.name }}

{{ collection.description }}

{{ collection.name }} editor: [{{ collection.editor }}]({{ collection.editorLink }})
{% endcapture %}

{{ collection-content | markdownify }}

{% assign dataFile = collection['volumes'] %}
{% assign gridLimit = 2 %}
{% include global/grid-generator.html heading="h4" %}
      </div>
{% endfor %}

{% comment %}
<div role='tabpanel' id='tabpanel-lifestyle' aria-labelledby='tab-lifestyle'>
### collection name


collection description.

collection name editor: editor and editor link

        {% assign dataFile = site.data.volumes.guide %}
        {% assign gridOffset = 3 %}
        {% include global/grid-generator.html heading="h4" %}
        </div>

<div role='tabpanel' id='tabpanel-training' aria-labelledby='tab-training'>
collection name

collection description

editors

          {% assign dataFile = site.data.volumes.guide %}
          {% assign gridOffset = 5 %}
          {% include global/grid-generator.html heading="h4" %}
        </div>
{% endcomment %}

{% include global/script-for-tabs.html selectedTabID="science" %}