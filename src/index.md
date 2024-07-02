---
layout: default
title: Project27 Skills - Skills that matter
tagline: A skill studio for disabled talents
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2024-02-04
hero-image: /assets/images/covers/tulips-cover.jpeg
hero-image-description: Daniel and Danielle are standing on a platform, with vast fields of colourful tulips and a canal in the background. Both of them smile at the camera.
pitch: We enable blind or learning disabled young people to experience flow, while they are developing skills that matter for professional development and personal growth, through our learning platform, community support, and principles of entrepreneurship.
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
listOfIcons: [["fas fa-pencil-alt", ""], ["fas fa-compass", ""], ["fa-solid fa-handshake", ""], ["fa-solid fa-person-chalkboard", ""], ["fas-lightbulb", ""]]
---

{% assign home = site.data.main['Home'] %}
{% assign guide = site.data.main['Guide'] %}

## What we do

We are a Brighton based social enterprise, serving a digital community of blind or learning disabled young people.
Our work focuses on **accessible {{ guide[0].name | downcase }}**, **enabling {{ guide[1].name | downcase }}**, and **inclusive education & employment**.

{% include global/cover-image.html image="networking-cover.jpg" alt="Holding his white cane, Daniel is standing in front of a wall full of people's photos, grouped into 'Entrepreneurship', 'Future of talent', 'Innovate education' and 'Partnership'.
" %}

Our co-founders - [Daniel]({% link about/team/Daniel/index.html %}) and [Danielle]({% link about/team/Danielle/index.html %}) - draw on lived experiences of disability, and professional skills in community engagement.
Daniel is a scientifically-minded blind person, with an interest in social entrepreneurship.
Danielle is a sociable learning disabled person, with an interest in art, media, gaming, and self-advocacy.

{% include global/buttonLink.html url="/about/index.html" label="Read more about us" %}

### Our community services

We have a range of services to meet the needs of our community, from trainees, through parents, to researchers and businesses.
Read what people say, before browsing our service offer below..

{% assign dataFile = site.data.testimonials %}
{% include global/carousel.html carouselDescription="A carousel of testimonials" %}

{% assign dataFile = home['services'] %}
{% assign gridLimit = 4 %}
{% include global/grid-generator-2.html heading="h4" %}

---

{% include spotlight.html %}