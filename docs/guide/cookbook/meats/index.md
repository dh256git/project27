---
layout: cookbook
title: Menu for meat feasts
---
<div class="container">
{% for post in site.categories.meats %}
{% include global/preview.html %}
{% endfor %}
</div>