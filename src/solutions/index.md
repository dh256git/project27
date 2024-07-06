---
layout: solutions
title: Project27 Solutions - Solutions that work
tagline: A co-design partner for disability inclusion
hero-image: /assets/images/covers/solutions-cover.jpg
hero-image-description: Daniel and Danielle are standing in front of a wall displaying eight speechbubbles. The following text is visible, 'Impact through effective partnership management',  'Fundamentals 360 view of business cooperation', 'business entrepreneurship', 'Creating startups', 'Developing entrepreneurial minds', 'Up for impactful research', 'Strategic partnerships' and 'for impact'.
pitch: We co-design and diffuse accessibility solutions in partnership with researchers and small businesses.
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2023-06-24
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
---

{% assign home = site.data.main['Home'] %}
{% assign guide = site.data.main['Guide'] %}

## What we do

We are a Brighton based social enterprise, serving a digital community of blind or learning disabled young people.
Our work focuses on **accessible {{ guide[0].name | downcase }}**, **enabling {{ guide[1].name | downcase }}**, and **inclusive education & employment**.

Our co-founders - [Daniel]({% link about/team/Daniel/index.html %}) and [Danielle]({% link about/team/Danielle/index.html %}) - draw on lived experiences of disability, and professional skills in research and innovation.
Daniel works in the disability innovation space, supporting early career researchers and start-up founders in translating ideas into opportunities for positive impact.
Danielle works with local councils, researchers, and charitable organisations as an accessibility and self-advocacy consultant within the learning disability domain.

{% include global/buttonLink.html url="/about/index.html" label="Read more about us" %}

## Our research and innovation services

Our research and innovation services are anchored in partnerships across academia and industry.
We offer a bespoke partnership model; consulting, collaborating, or co-creating according to individual needs of research groups and small businesses.
Read what people say, before browsing our service offer below..

{% assign dataFile = site.data.testimonials-for-solutions %}
{% include global/carousel.html carouselDescription="A carousel of testimonials" %}

{% assign dataFile = home['services'] %}
{% assign gridOffset = 4 %}
{% include global/grid-generator-2.html heading="h3" %}