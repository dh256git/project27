---
layout: recipes
title: Menu for pasta dishes
---

  <ul>
    {% for post in site.categories.pastas %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
