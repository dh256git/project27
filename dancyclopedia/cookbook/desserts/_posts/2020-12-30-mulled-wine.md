---
layout: desserts
title: Mulled wine
menu: desserts
video: https://youtu.be/PfHMCB7UePc
---

Let's see how to cook your chosen dish.

## Ingredients

Here is what you need to have at home.

<table>
  {% for row in site.data.cookbook.desserts.mulled-wine%}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>

## Preparation

Time: Takes as long as it takes.  
Serves: Make sure to share, and buy for your pals.

Here are the steps to cook the meal. Enjoy!

1. Start playing music in the background.
2. Pore a glass of drink for the chef.
3. Start heating up the wine at low heat.
4. Crush the cinnamon stick into the wine, and chuck a handful of cloves into it.
5. Zest orange skin into it, and squeeze the juice of the orange into the wine.
6. Stir and add the sugar.
7. Finally add the plums and water and wait until it heats up again.
8. Serve into mugs with a few plums.