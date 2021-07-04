---
layout: cookbook
title: Menu for salads and dips
---
<div class="container">
{% for post in site.categories.salads %}
{% include global/preview.html %}
{% endfor %}
</div>