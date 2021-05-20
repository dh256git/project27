---
layout: default
title: Menu for wraps and rolls
---

{% for post in site.categories.wraps %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}