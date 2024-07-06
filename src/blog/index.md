---
layout: default
title: Stories
tagline: The impact of social participation on our lives
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-09-01
licence: copyright
buttonStyle: fg-blog-land
backgroundStyle: bg-blog-land
levelToOpen: volume
tabpanelIDList: ["science", "lifestyle"]
pitch: We help young disabled people and their parents or carers to find encouraging examples of personal growth and professional development, through sharing our lived experience of sight loss, learning disability, and success in a series of joyful blog posts.
hero-image: /assets/images/covers/blog-cover.jpg
hero-image-description: A person writing into a journal with a pen.
---

{% assign stories = site.data.main['Stories'] %}

### What stories are we sharing?

Our blog is intended for anyone who may wish to take inspiration from the experiences of our community. We have two collection of posts: lifestyle and science & technology. The latter shares experiences of blind individuals learning about web design, creating accessible science content, and emerging technologies used for accessibility, such as generative artificial intelligence. Topics include web design challenges and accessibility solutions, as well as issue tracking specific to our own web development journey.

We also discuss living with disabilities through the lens of personal adventures, identity exploration, and social participation. Topics cover diverse experiences, from daily activities to extraordinary journeys, and the importance of understanding multifaceted identities. We also delve into the power of reading and special interests like entrepreneurship and self-advocacy.

<div role='tablist'>
{% for collection in stories %}
{% assign collectionIndex = forloop.index | minus: 1 %}
    <button role='tab' id='tab-{{ page.tabpanelIDList[collectionIndex] }}' aria-controls='tabpanel-{{ page.tabpanelIDList[collectionIndex] }}' onClick="setTab('{{ page.tabpanelIDList[collectionIndex] }}')">{{ collection.name }}</button>
{% endfor %}
    </div>

{% for collection in stories %}
{% assign collectionIndex = forloop.index | minus: 1 %}
<div role='tabpanel' id='tabpanel-{{ page.tabpanelIDList[collectionIndex] }}' aria-labelledby='tab-{{ page.tabpanelIDList[collectionIndex] }}'>
{% capture collection-content %}
## Stories in {{ collection.name }}

{{ collection.description }}

{{ collection.name }} editor: [{{ collection.editor }}]({{ collection.editorLink }})
{% endcapture %}

{{ collection-content | markdownify }}

{% assign dataFile = collection['volumes'] %}
{% include global/grid-generator.html heading="h3" %}
      </div>
{% endfor %}

{% include global/script-for-tabs.html selectedTabID="lifestyle" %}

<hr>
{% include spotlight.html %}