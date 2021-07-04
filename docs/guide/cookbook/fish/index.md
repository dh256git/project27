---
layout: cookbook
title: Menu for fish and sea food
---
<div class="container">
{% for post in site.categories.fish %}
{% include global/preview.html %}
{% endfor %}
</div>