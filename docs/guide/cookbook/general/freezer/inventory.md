---
layout: default
title: Inventory of freezer
---

This is what I have in the freezer.

<table>
  {% for row  in site.data.cookbook.freezer %}
{% include global/tabulator.html %}
  {% endfor %}
</table>