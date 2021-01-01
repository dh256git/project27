---
layout: recipesdefault
title: Menu for wraps
---

  <ul>
    {% for post in site.categories.wraps %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
