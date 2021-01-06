---
layout: default
title: Menu for fish dishes
---

  <ul>
    {% for post in site.categories.fish %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>

### To do

* Fried salmon filet
