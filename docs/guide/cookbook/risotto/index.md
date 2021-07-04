---
layout: cookbook
title: Menu for risotto
---
<div class="container">
{% for post in site.categories.risotto %}
{% include global/preview.html %}
{% endfor %}
</div>