---
layout: cookbook
title: Menu for meat feasts
---
<div class="container">
{% for post in site.categories.meats %}
{% include guide/cookbook-menu.html %}
{% endfor %}
</div>