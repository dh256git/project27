---
layout: cookbook
title: Menu for pasta dishes
---
<div class="container">
{% for post in site.categories.pastas %}
{% include global/preview.html %}
{% endfor %}
</div>