---
layout: cookbook
title: Menu for risotto
---
<div class="container">
{% for post in site.categories.risotto %}
{% include guide/cookbook-menu.html %}
{% endfor %}
</div>