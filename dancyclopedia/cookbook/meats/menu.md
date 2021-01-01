---
layout: recipes
title: Menu for meat feast
---

  <ul>
    {% for post in site.categories.meats %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
