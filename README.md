---
layout: default
title: About Project27
---
# About {{ site.brand }}

This page introduces the {{ site.brand }} vision and mission, why it exists, who is behind the content, and what the roadmap of development is.

---

## Who is behind {{ site.brand }}?

Welcome, my name is Daniel, and the {{ site.brand }} vision is my vision too. 

I lost my sight at the age of 16. Yet, I live a good life.
I have a doctorate degree in science, I have a healthy social life, and I live independently.
My journey was not easy, but it was doable with support and the right mindset.
So now, I would like to help those who are at the beginning of their journey.
This is why I created {{ site.brand }}.

The {{ site.brand }} Blog is where I express my opinion, insights, and experiences.
The {{ site.brand }} {{ site.product }} is where I publish scribbles on technical and lifestyle challenges I have once faced, and the solutions that helped me overcome these challenges.

{{ site.brand }} is really a warehouse of challenges and solutions.
I truly wish that the content and the spirit of {{ site.brand }} will become not only my own, but a shared vision of many.

So long, all the best!  
Daniel

[Read the complete welcome letter by Daniel, and get to know him more](./about/author.html)

---

## The modest ambition

On the small scale, {{ site.brand }} is a private, digital notebook on a range of topics that matter to the author. It is a hobby activity, an opportunity to learn skills in web development, audio editing, and revising notes on physics.

[Read more about the modest ambition](./about/modest.html)

---

## The grand ambition

However, there exists a vision on the grand scale too.

[Read more about the grand ambition](./about/grand.html)

---

## What's on {{ site.brand }}?

The site is split into two parts: [Blog](./blog/index.html) and [{{ site.product }}.](./guide/index.html)
Blog posts and {{ site.product }} scribbles both come in two flavours: technical, and lifestyle. 

The blog has two branches: [LogBook](./blog/logbook/index.html) and [TWIST.](./blog/twist/index.html)

The {{ site.product }} is what I think about as an educational, web journal.
Initially, five volumes, separated into two collections, form part of the {{ site.product }}.

1. Science collection:
 * [Mathematical and Physical Sciences (MPS);](./guide/MPS/index.html)
 * [Computer Literacy;](./guide/CL/index.html)
 * [Statistics;](./guide/statistics/index.html)
2. Lifestyle collection:
 * [Cookbook;](./guide/cookbook/index.html)
 * [Vocal.](./guide/vocal/index.html)

[Read more about what you will find on this site](./about/content.html)

---

## Where does the {{ site.brand }} roadmap lead?

The roadmap of this project is split into five year intervals.

{% capture rm2025 %}
 {{ site.brand }} is a private tool, under construction.
 No public access is granted.
 In the first five years, the key characteristics and targets are:
</p>
<ul>
<li>single author project, with smaller contributions from trusted friends.</li>
<li>learn basic web development skills,</li>
<li>explore solutions and methods around accessible written technical content creation, and</li>
<li>expand the library of scribbles with written content, external links, and multimedia.</li>
</ul>
<p>
The key performance indicators are:
</p>
<ul>
<li>A coherent, usable, easy to maintain website architecture is completed;</li>
<li>a solution is regularly executed and documented for deploying content that is universally accessible on Windows, Mac, and iOS, using automated conversion of markup sources, and clutter cleaner scripts, eliminating the use of any additional need for processing published content;</li>
<li>every volume, chapter, and blog topic has at least one high quality, complete article;</li>
<li>KPIs are determined for 2025-2030.</li>
</ul>
<p>Moving on...
{% endcapture %}

{% capture rm2030 %}
For the second interval of five years, the project is in public beta status to inform its roadmap, potentially introducing a pivot point.
</p>
<ul>
<li>Two author project: Daniel and a co-editor works together to conform the content and web architecture to public feedback.</li>
<li>exploration of solutions for appending graphical and video content with their non-visual equivalence;</li>
<li>expand scribbles in existing volumes, and consider new volumes based on feedback.</li>
</ul><p>
Moving on...
{% endcapture %}

{% capture rm2035 %}

Ten years after conception, {{ site.brand }} transitions from a single author project to a multi-author journal. 
</p>
<ul>
<li>The CEO oversees the content creation, funding and marketing tasks. The CTO is responsible for quality assurance of the web architecture including accessibility and functionality, as well as exploring new technological solutions in line with the vision and mission statements;</li>
<li>associate editors are appointed to take care of individual volumes;</li>
<li>volume content is expanded by the project team, and public feedback based on usage is considered; however, still no public notes are published;</li>
<li>a system is developed for submitting scribbles by the public, and distributed for peer review.</li>
</ul><p>
Moving on...
{% endcapture %}

{% capture rm2050 %}
The web journal opens for public submission of scribbles, which are published after peer review and quality check.
</p>
<ul>
<li>operation starts as conventional journals with editor, associate editors, reviewers, and authors;</li>
<li>strategy development for revenue making from tools developed and experiences from the past 15 years;</li>
<li>journal remains open source.</li>
</ul><p>
If the project has got as far as this, the roadmap will be extended.
{% endcapture %}

{% include global/collapseable.html trigger="2025" paragraph=rm2025 ID="2025rm" %}
{% include global/collapseable.html trigger="2030" paragraph=rm2030 ID="2030rm" %}
{% include global/collapseable.html trigger="2035" paragraph=rm2035 ID="2035rm" %}
{% include global/collapseable.html trigger="2035-2050" paragraph=rm2050 ID="2050rm" %}

### Evolution of contributions

For now, in the first five years from 2020, I will explore solutions and write content  on my own.
However, eventually, I'd like to have associate editors, who take care of existing content and expand the volume they own.
Although one of the key objective at the personal level is to learn web development, I'd like to work with a web developer, occupying the role of CTO, who knows what they are doing and are able to innovate through modern technological solutions.
I'm just writing web scribbles and work towards the vision step by step. 

### Issue tracking

{{ site.brand }} will track known issues on inaccurate information, as well as known accessibility bugs around the scientific content.
This will partly be done through the GitHub repository and the LogBook posts.
