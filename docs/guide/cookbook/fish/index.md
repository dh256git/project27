---
layout: cookbook
title: Menu for fish and sea food
---
<div class="container">
{% for post in site.categories.fish %}
{% include guide/cookbook-menu.html %}
{% endfor %}
</div>