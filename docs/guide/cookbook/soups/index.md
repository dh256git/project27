---
layout: cookbook
title: Menu for soups
---
<div class="container">
{% for post in site.categories.soups %}
{% include guide/cookbook-menu.html %}
{% endfor %}
</div>