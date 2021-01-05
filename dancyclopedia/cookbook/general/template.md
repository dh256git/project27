---
layout: recipes
title: 
menu: 
video: 
music: 
additional:
  - name: 
    link: 
  - name: 
    link: 
time: Takes as long as it takes.
serves: Make sure to share, and buy for your pals.
---

Short description of the meal.

## Ingredients

Here is what you need to have at home.

<table>
  {% for row  in site.data.cookbook.desserts.** %}
{% include ingredients.html %}
  {% endfor %}
</table>

Serves: {{ page.serves }}

## Preparation

Here are the steps to cook the meal. {{ page.time }} Share and enjoy!

1. Play music in the kitchen. [I recommend this playlist.]({{ page.music }})
2. Pore a glass of drink for the chef.
3. 