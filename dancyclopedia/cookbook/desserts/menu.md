---
layout: recipes
title: Menu for desserts and breakfast
---

  <ul>
    {% for post in site.categories.desserts %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>

### To do

* Fruit baskets

* crumpet with spreads
* scrambled eggs
* frittata
* baked beans with sausages
* leek, lardon, camembert dish
* smoked salmon with cream cheese