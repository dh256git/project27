---
layout: default
title: Menu for soups
---
  <ul>
    {% for post in site.categories.soups %}
      <li><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
