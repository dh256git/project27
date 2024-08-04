---
layout: default
author: Daniel Hajas
title: All of our stories
buttonStyle: fg-blog-sect
backgroundStyle: bg-blog-sect
pitch: Find all of our stories on one page. Nothing new, but it's convenient on when you are not looking for a specific topic.
---

{% assign categoryLink = '' %}
{% assign devLink = '/blog/logbook/dev/index.html' %}
{% assign issuesLink = '/blog/logbook/issues/index.html' %}
{% assign latexLink = '/blog/logbook/LaTeX-to-MathML/index.html' %}
{% assign mathmlLink = '/blog/logbook/MathML-usability/index.html' %}
{% assign disabilitiesLink = '/blog/twist/disabilities/index.html' %}
{% assign identitiesLink = '/blog/twist/identities/index.html' %}
{% assign nanotipLink = '/blog/twist/nanotip/index.html' %}
{% assign readingLink = '/blog/twist/reading/index.html' %}
{% assign specialLink = '/blog/twist/special-interests/index.html' %}

### Story feed

<div class="container mt-5">
{% for post in site.posts %}
{% if post.url contains "guide" or post.url contains "grapheel" or post.url contains "news" %}
{% continue %}
{% endif %}
<div class="row news-item">
<div class="col-12 col-md-3">
{% if post.image %}
<img src="{{ '/assets/images' | append: post.image | prepend: site.baseurl }}" alt="{{ post.alt }}" class="news-thumbnail img-fluid">
{% else %}
<img src="{{ '/assets/images/Project27 logo.png' | prepend: site.baseurl }}" alt="A placeholder image, showing the Project27 logo." class="news-thumbnail img-fluid">
{% endif %}
</div>
<div class="col-12 col-md-9">
<h4><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h4>
<p class="mb-1">Posted in 
{% if post.url contains "/dev/" %}
{% assign categoryLink = devLink %}
{% elsif post.url contains "issues" %}
{% assign categoryLink = issuesLink %}
{% elsif post.url contains "latex-to-mathml" %}
{% assign categoryLink = latexLink %}
{% elsif post.url contains "mathml-usability" %}
{% assign categoryLink = mathmlLink %}
{% elsif post.url contains "disabilities" %}
{% assign categoryLink = disabilitiesLink %}
{% elsif post.url contains "identities" %}
{% assign categoryLink = identitiesLink %}
{% elsif post.url contains "nanotip" %}
{% assign categoryLink = nanotipLink %}
{% elsif post.url contains "reading" %}
{% assign categoryLink = readingLink %}
{% elsif post.url contains "special-interests" %}
{% assign categoryLink = specialLink %}
{% else %}
{% assign categoryLink = '/404.html' %}
{% endif %}
<a href="{{ categoryLink | prepend: site.baseurl }}">
{{ post.tag }}
</a>
, on {{ post.date | date_to_rfc822 | date: "%d %b %Y" }}.</p>
</div>
</div>
{% endfor %}
</div>