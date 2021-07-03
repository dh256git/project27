---
layout: cookbook
title: Menu for pasta dishes
---
<div class="container">
{% for post in site.categories.pastas %}
{% include guide/cookbook-menu.html %}
{% endfor %}
</div>