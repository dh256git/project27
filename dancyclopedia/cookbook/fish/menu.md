---
layout: default
title: Menu for fish and sea food
---

{% for post in site.categories.fish %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}