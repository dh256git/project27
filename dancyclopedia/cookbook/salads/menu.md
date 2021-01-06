---
layout: default
title: Menu for salads
---

  <ul>
    {% for post in site.categories.salads %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
