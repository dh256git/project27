---
layout: default
title: Menu for pasta dishes
---

{% for post in site.categories.pastas %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}