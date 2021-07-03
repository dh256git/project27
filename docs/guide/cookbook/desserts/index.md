---
layout: cookbook
title: Menu for desserts and brekfast
---
<div class="container">
{% for post in site.categories.desserts %}
{% include guide/cookbook-menu.html %}
{% endfor %}
</div>