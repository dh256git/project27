---
layout: default
title: News archive
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-16
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
pitch: Find all of our news in one convenient place. Want to receive our quorterly newsletter straight in your inbox? Sign up in the footer.
---

<div class="container mt-5">
{% for news in site.data.news %}
<div class="row news-item">
<div class="col-12 col-md-3">
<img src="{{ '/assets/images/news/' | append: news.thumbnail | prepend: site.baseurl }}" alt="{{ news.thumbnailAlt }}" class="news-thumbnail img-fluid">
</div>
<div class="col-12 col-md-9">
<h4><a href="{{ news.link | prepend: site.baseurl }}">{{ news.headline }}</a></h4>
<p class="mb-1">{% if news.teaser %}{{ news.teaser }}{% endif %}</p>
<small class="text-muted">{{ news.date | date_to_rfc822 | date: "%d %b %Y" }}</small>
</div>
</div>
{% endfor %}
</div>