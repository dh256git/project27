---
layout: default
title: Menu for meat feasts
---

{% for post in site.categories.meats %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}