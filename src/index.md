---
layout: default
title: Project27 Home Page
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2023-01-21
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
listOfIcons: [["fas fa-pencil-alt", ""], ["fas fa-compass", ""], ["fa-solid fa-handshake", ""], ["fa-solid fa-person-chalkboard", ""]]
---

## Why trust us

We help blind or learning disabled people to develop skills that matter.
{{ site.brand }} reduces the frustration caused by inaccessible learning tools, and builds confidence in your abilities.
We do this through peer support, personalised opportunities for learning, creating and discovering new challenges in a safe place, built by it's community.

{{ site.brand }} is developed by a couple - Daniel and Danielle.
We draw on our lived experiences and professional skills.
Daniel is a scientifically-minded blind person, with an interest in social entrepreneurship.
Danielle is a sociable learning disabled person, with an interest in art, media, gaming, and self-advocacy.

{% include global/buttonLink.html url="/about/index.html" label="Read more about us" %}

{% include spotlight.html %}

## What we do

We engage in a range of activities to support our mission.

1. **Sharing thoughts**: We share our lived experience of sight-loss, learning disability, and success, through our [blog.]({% link blog/index.html %})
2. **Passive learning**: We enable people to learn about science and lifestyle, by creating accessible articles in the [{{ site.brand }} {{ site.product }}.]({% link guide/index.html %})
3. **Active learning**: We promote active learning, by [getting volunteers involved]({% link volunteering/index.md %}) in building the [{{ site.brand }} {{ site.product }}.]({% link guide/index.html %})
4. **Consultancy**: Anyone who needs time to talk things through with us can [book a support session]({% link support/index.md %}) for a session of consulting, tutoring, or mentoring.
5. **Research and innovation**: We work with academic researchers and businesses to push the frontiers of access to science, and disability inclusion.

---

{% assign dataFile = site.data.navigation %}
{% include global/grid-generator.html heading="h3" %}
