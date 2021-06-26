---
layout: default
title: Menu for soups
---
<div class="container">
{% for post in site.categories.soups %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}
</div>