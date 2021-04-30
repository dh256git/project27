---
layout: default
title: Menu for risotto
---

{% for post in site.categories.risotto %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}