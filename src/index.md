---
layout: default
title: Project27 Skills - Skills that matter
tagline: The skill studio for disabled talents
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2024-07-04
hero-image: /assets/images/covers/tulips-cover.jpeg
hero-image-description: Daniel and Danielle are standing on a platform, with vast fields of colourful tulips and a canal in the background. Both of them smile at the camera.
pitch: We create personalised pathways of experiential training and professional development opportunities for blind and learning-disabled individuals. Through our community-driven learning resources and co-working platform, we provide a safe-space and tailored support to help members develop valuable skills, find their passions, and succeed in the job market, such that they can grow personally and professionally at the pace that suits them.
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
---

{% assign home = site.data.main['Home'] %}
{% assign guide = site.data.main['Guide'] %}

## Who we are

"We are a social enterprise based in Brighton, led by and serving a global digital community of blind and learning disabled individuals who embrace a growth mindset through discovery, learning, and co-creation."

Our co-founders - [Daniel]({% link about/team/Daniel/index.html %}) and [Danielle]({% link about/team/Danielle/index.html %}) - draw on lived experiences of disability, and professional skills in community engagement.
Daniel is a scientifically-minded blind person, with an interest in social entrepreneurship.
Danielle is a sociable learning disabled person, with an interest in art, media, gaming, and self-advocacy.

{% include global/buttonLink.html url="/about/index.html" label="Read more about us" %}

## What we do

Our community services and fields of interest are complementary to the value created by mentorship organisations, parent support groups, and training or employment support services.

{% capture interests %}
### Our fields of interest

We focus on developing analytical and digital skills that matter to blind people interested in {{ guide[0].name | downcase }}, for example studying mathematics, practicing web design, or working in accounting.

In addition, we also develop social and media skills that matter to neurodiverse people  interested in a joyful {{ guide[1].name | downcase }}.
{% endcapture %}

{% include global/image-with-text.html left-column="6" right-column="6" text=interests image="/covers/networking-cover.jpg" alt="Holding his white cane, Daniel is standing in front of a wall full of people's photos, grouped into 'Entrepreneurship', 'Future of talent', 'Innovate education' and 'Partnership'.
" width="100%" height="100%" %}

### Our community services

We offer varying levels of engagement and support for different stages of self-development.
Our community services are tailoured to the interaction needs of individuals, and their level of disability awareness or learning style.

Read what people say about our community services, before browsing the ways we create value..

{% assign dataFile = site.data.testimonials %}
{% include global/carousel.html carouselDescription="A carousel of testimonials" %}

{% assign dataFile = home['services'] %}
{% assign gridLimit = 4 %}
{% include global/grid-generator-2.html heading="h4" %}

---

{% include spotlight.html %}