---
layout: default
title: Menu for pasta dishes
---
<div class="container">
{% for post in site.categories.pastas %}
<h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
<p>{{ post.excerpt }}</p>
{% endfor %}
</div>