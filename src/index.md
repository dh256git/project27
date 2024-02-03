---
layout: default
title: Project27 - Skills that matter
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2024-02-04
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
listOfIcons: [["fas fa-pencil-alt", ""], ["fas fa-compass", ""], ["fa-solid fa-handshake", ""], ["fa-solid fa-person-chalkboard", ""], ["fas-lightbulb", ""]]
---

{% assign home = site.data.main['Home'] %}
{% assign guide = site.data.main['Guide'] %}

We enable blind or learning disabled young people to experience [flow](https://www.ted.com/talks/mihaly_csikszentmihalyi_flow_the_secret_to_happiness?language=en), while they are developing skills that matter for professional development and personal growth, through our learning platform, community support, and principles of entrepreneurship.

## What we do

We are a Brighton based social enterprise, serving a digital community of blind or learning disabled young people.
Our work focuses on **accessible {{ guide[0].name | downcase }}**, **enabling {{ guide[1].name | downcase }}**, and **inclusive education & employment**.

{% include global/cover-image.html image="founders-cover.jpg" alt="Daniel and Danielle are photographed in the UK Parliament. They are wearing smart clothing. A guide dog is sitting in front of them. In the background multiple signs are visible, such as logos of University College London, World Health Organisation, and GDI Hub. Other signs read 'AT changes lives' and 'Launching the Global Report on Assistive Technology'." %}

Our co-founders - [Daniel]({% link about/team/Daniel/index.html %}) and [Danielle]({% link about/team/Danielle/index.html %}) - draw on lived experiences of disability, and professional skills in community engagement.
Daniel is a scientifically-minded blind person, with an interest in social entrepreneurship.
Danielle is a sociable learning disabled person, with an interest in art, media, gaming, and self-advocacy.

{% include global/buttonLink.html url="/about/index.html" label="Read more about us" %}

## Our products and services

We have a range of services to meet the needs of our community, from trainees, through parents, to researchers and businesses.
Read what people say, before browsing our service offer below..

{% assign dataFile = site.data.testimonials %}
{% include global/carousel.html carouselDescription="A carousel of testimonials" %}

{% assign dataFile = home['services'] %}
{% include global/grid-generator-2.html heading="h3" %}

{% include spotlight.html %}
