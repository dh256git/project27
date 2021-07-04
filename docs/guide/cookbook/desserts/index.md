---
layout: cookbook
title: Menu for desserts and brekfast
---
<div class="container">
{% for post in site.categories.desserts %}
{% include global/preview.html %}
{% endfor %}
</div>