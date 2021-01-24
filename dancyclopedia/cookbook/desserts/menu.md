---
layout: default
title: Menu for desserts and brekfast
---

{% for post in site.categories.desserts %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}