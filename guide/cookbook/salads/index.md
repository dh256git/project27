---
layout: default
title: Menu for salads and dips
---

{% for post in site.categories.salads %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}