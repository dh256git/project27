---
layout: recipes
title: Menu for risotto meals
---

  <ul>
    {% for post in site.categories.risotto %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>