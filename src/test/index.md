---
layout: default
title: Test
tagline: Together we learn, together we grow
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-10-02
licence: copyright
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
myList: ["apple", "orange", "banana"]
---

## {{ page.title }}


{% for item in page.myList %}
{% assign myIndex = forloop.index | minus: 1 %}
{{ page.myList[myIndex] }}, 
{% endfor %}



{% assign main = site.data.main %}

{% assign science =  main['Guide'][0] %}

{{ main['Guide']['overview'] }}

### {{ science['name'] }}

{% for volume in science['volumes'] %}
[{{ volume.name }}]({{ volume.link }}),
{% endfor %}