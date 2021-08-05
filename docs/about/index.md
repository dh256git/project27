---
layout: default
title: About Project27
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
listOfIcons: [["", ""], ["", ""]]
---
# About {{ site.brand }}

This page introduces the {{ site.brand }} vision and mission, why it exists, who is behind the content, and what the roadmap of development is.

---

## Who is behind {{ site.brand }}?

{{ site.brand }} was started by a blind science graduate, called Daniel. He develops the project, with the help of contributions made by  his friends, family members, and colleagues.

---

> Welcome, my name is Daniel, and the {{ site.brand }} vision is my vision too. 
> 
> I lost my sight at the age of 16. Yet, I live a good life.
I have a doctorate degree in science, I have a healthy social life, and I live independently.
My journey was not easy, but it was doable with support and the right mindset.
So now, I would like to help those who are at the beginning of their journey.
This is why I created {{ site.brand }}.
> 
> The {{ site.brand }} Blog is where I express my opinion, insights, and experiences.
The {{ site.brand }} {{ site.product }} is where I publish scribbles on technical and lifestyle challenges I have once faced, and the solutions that helped me overcome these challenges.
> 
> {{ site.brand }} is really a warehouse of challenges and solutions.
I truly wish that the content and the spirit of {{ site.brand }} will become not only my own, but a shared vision of many.
> 
> So long, all the best!  
> Daniel

---

[View Daniel's profile to read the complete welcome letter](./author.html)

## The modest ambition

In the short run, {{ site.brand }} is a digital, private notebook on a range of topics that matter to the author. It is a hobby activity and an opportunity to learn new skills and practice existing ones.

[Read more about the modest ambition](./modest.html)

## The grand ambition

However, there exists a vision on the grand scale too.
In the long run, the single author corpus is expanded to a collection of peer-written and peer-reviewed content.
The topics of the product owner's personal interest are expanded to community interest.

[Read more about the grand ambition](./grand.html)

## Values and culture

The culture at {{ site.brand }} is defined by four core values:

1. commitment,
2. openness,
3. respect, and
4. engagement.

[Read more about our values](./values.html)

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

[Read more about what you will find on this site](./content.html)

## Where does the {{ site.brand }} roadmap lead?

The roadmap of {{ site.brand }} starts on 6th of October, 2019 with setting the cornerstone.
The road ahead is made up of four milestones, separated by five year intervals.

{% capture rm2020 %}
Collecting physics notes and recipes scattered around the hard-drive into a single,  accessible, and usable platform.
{% endcapture %}

{% capture rm2025 %}
<h4>2025 milestone</h4></p>
<p>
Theme: Development of a private site based on product requirements of the product owner.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Team: {{ site.brand }} is developed by the product owner. Contributions are made by trusted friends and family.</li>
<li>R&D: Learning basic web development skills, and developing v0.1.</li>
<li>PM&BD: Learning basic project management and business development skills, and setting a workflow up.</li>
<li>R&D: Documenting the challenges and solutions occurred during the experimentation with methods of creating accessible content for  technical documents.</li>
<li>Content: Expanding original content with reviewed written notes and posts, external links, and external multimedia.</li>
</ul>
<p>
The key performance indicators are:
</p>
<ul>
<li>How much do people in the organisation engage with the initiatives of the current milestone?</li>
<li>Is {{ site.brand }} a stable release of a coherent, usable, and easy-to-maintain website architecture?</li>
<li>Are basic project management procedures and business development strategies established in a sustainable framework?</li>
<li>How regularly are R&D challenges and solutions executed and documented?;</li>
<li>How many reviewed "notes" and "posts" are published in individual Guide "chapters", and Blog "categories" respectively?</li>
<li>Does the next milestone and its initiatives reflect the latest requirements, and are KPIs updated?</li>
</ul>
<p>Moving on...
{% endcapture %}

{% capture rm2030 %}
<h4>2030 milestone</h4></p>
<p>
Theme: Pivoting towards requirements set by stakeholders.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Team: The product owner and a business partner works together to adapt the product to new requirements set by stakeholders. Contributions are made by three {{ site. brand }} teams: the R&D team, the editorial and review team, and the content creation team.</li>
<li>R&D: Exploring challenges and solutions for accessible data visualisations, figures, and videos of technical nature.</li>
<li>Content: Expanding notes and posts in existing volumes and branches. Considering new volumes based on stakeholder requirements.</li>
</ul><p>
Moving on...
{% endcapture %}

{% capture rm2035 %}
<h4>2035 milestone</h4></p>
<p>
Theme: Consolidating operations.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Team: Establishing organisational structure. The CEO oversees the content creation, funding and marketing tasks. The CTO is responsible for quality assurance of the web architecture including accessibility and functionality, as well as exploring new technological solutions in line with the vision and mission statements.</li>
<li>Community: associate editors are appointed to take care of individual volumes, and content authors are recruited for creative and review tasks.</li>
<li>Content: Volumes are expanded by content authors. User requirements are used to design content.</li>
<li>R&D: A system is developed for submitting user authored content and its distribution for peer-review.</li>
</ul><p>
Moving on...
{% endcapture %}

{% capture rm2050 %}
<h4>2050 milestone</h4></p>
<p>
Theme: {{ site.brand }} opens for public contributions, which are published after peer-review.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Community: Operation starts as conventional journals with editor, associate editors,-reviewers, and authors.</li>
<li>PM&BD: Strategy is developed for harnessing revenue streams from the tools developed and the team expertise, reinvesting in advancing {{ site.brand }} R&D initiatives.</li>
</ul><p>
If the project has got as far as this, the roadmap will be extended.
{% endcapture %}

{% include global/collapseable.html trigger="2020 cornerstone" paragraph=rm2020 ID="R2020" %}
{% include global/collapseable.html trigger="2025 milestone" paragraph=rm2025 ID="R2025" %}
{% include global/collapseable.html trigger="2030 milestone" paragraph=rm2030 ID="R2030" %}
{% include global/collapseable.html trigger="2035 milestone" paragraph=rm2035 ID="R2035" %}
{% include global/collapseable.html trigger="2050 milestone" paragraph=rm2050 ID="R2050" %}

### Evolution of contributions

The time between the cornerstone and the first milestone is used to learn, experiment, and set the scene for a scalable project.
The project is primarily a one person exploration.
Although one of the key objective at the personal level is to learn web development, expanding the R&D team with a web developer who knows what they are doing and are able to innovate through modern technological solutions, would be desirable.

The second milestone introduces the project and its stakeholders to each other, updating product requirements, with a business partner on board.
The PM&BD team is formed.

The third milestone transfers ownership parts of the product to associate editors, and reviewers are recruited to make up the {{ site.brand }} community.
Content is heavily influenced by user requirements.

In the final milestone, the project is community driven, by means of peer-reviewed contributions. Content is managed by associate editors, while the management team looks after sustainability, scalability, and reinvestment in R&D initiatives.

### Issue tracking

{{ site.brand }} will track known issues on inaccurate information, as well as known accessibility bugs around the scientific content.
This will partly be done through the GitHub repository and the LogBook posts.
