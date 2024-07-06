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
levelToOpen: volume
tabpanelIDList: ["science", "lifestyle", "training"]
pitch: We enable blind or learning disabled people to learn and develop new skills in science, technology, lifestyle, and  media on their own, through a collection of accessible learning resources.
hero-image: /assets/images/covers/guide-cover.jpg
hero-image-description: Someone is holding a paper map, and pointing at a location with a finger.
---

{% assign guide = site.data.main['Guide'] %}

### What does the {{ site.product }} say?

Our {{ site.product }} helps blind or learning disabled people to access learning resources, even if you don't want to join our community.
The screen reader accessible, and easy read notes enable you to develop and practice new skills in your own time, at no cost.
We promote {{ guide[0].name | downcase }} skills, as well as self-advocacy through resources in our {{ guide[1].name | downcase }} collection.
The {{ site.product }} is intended to give direction to blind or learning disabled people, but you should use it as a starting point to learning and practicing new skills that interest you.

We organise notes into collections of volumes.
For example, recipes are included in our {{ guide[1]['volumes'][0].name }} {{ page.levelToOpen }}, in the {{ guide[1].name }} collection.
Our community members find exercises and host their personal projects in our {{ guide[2].name }} collection at the beginning of their skills development journey.
More experienced trainees, volunteers, and the core {{ site.org }} team edit the rest of our {{ site.product }}. 
Find a learning resource that you might be interested in, by selecting a tab below.

<div role='tablist'>
{% for collection in guide %}
{% assign collectionIndex = forloop.index | minus: 1 %}
    <button role='tab' id='tab-{{ page.tabpanelIDList[collectionIndex] }}' aria-controls='tabpanel-{{ page.tabpanelIDList[collectionIndex] }}' onClick="setTab('{{ page.tabpanelIDList[collectionIndex] }}')">{{ collection.name }}</button>
{% endfor %}
    </div>

{% for collection in guide %}
{% assign collectionIndex = forloop.index | minus: 1 %}
<div role='tabpanel' id='tabpanel-{{ page.tabpanelIDList[collectionIndex] }}' aria-labelledby='tab-{{ page.tabpanelIDList[collectionIndex] }}'>
{% capture collection-content %}
## The {{ collection.name }} collection

{{ collection.description }}

{{ collection.name }} editor: [{{ collection.editor }}]({{ collection.editorLink }})
{% endcapture %}

{{ collection-content | markdownify }}

{% assign dataFile = collection['volumes'] %}
{% assign gridLimit = 2 %}
{% include global/grid-generator.html heading="h3" %}
      </div>
{% endfor %}

{% include global/script-for-tabs.html selectedTabID="science" %}