---
layout: cookbook
title: Menu for soups
---
<div class="container">
{% for post in site.categories.soups %}
{% include global/preview.html %}
{% endfor %}
</div>