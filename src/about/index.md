---
layout: default
title: About us
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
pitch: At Project27, we help disabled individuals, their co-workers, and their employers develop practical skills relevant to the jobs they are passionate about, unlocking the potential for personal and professional growth. We also co-design solutions that enhance social participation across the entire value chain. We combine for-profit practices with nonprofit missions to create positive outcomes in a sustainable way.
licence: copyright
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

### Our vision

We envision a world where everyone has the opportunity for social and economic participation, ensuring that disabled individuals are included and benefit from personal and professional growth.

### Our mission

Our mission is to create personalised opportunities for skills development and pathways for personal and professional growth in a safe environment for communities of blind and learning disabled individuals.

### Our values and community culture

The community culture of {{ site.org }} can be expressed in a single word. We promote 'CARE', referring to 'commitment, accessibility, respect, and engagement'.

{% capture values %}
Our core values are:

1. Growth, encompassing curiosity and self-development, leading to new opportunities of discovery and achievement.
2. Sense of belonging, where everyone has a team member to go to for advice and mentorship.
3. Structure, enabling community members to follow processes, track and recognise progress, build on solid foundations, and spot missing elements.
4. Flow, referring to the ultimate experience of accessibility, barrier-free joy, creativity, and productivity, while engaging in a subject of passion, setting the right level of challenge. If this is a new concept to you, [watch this video on flow.](https://youtu.be/znwUCNrjpD4?si=-6k0xuaWMltD7rFH)
{% endcapture %}

{% include global/image-with-text.html left-column="6" right-column="6" text=values image="/general/values-word-cloud.png" alt="A word cloud of values printed in different font size, colour, and location. The largest words are growth, flow, sense of belonging. In smaller print, the words curiosity, self-development, and structure appear. In even smaller print, words like mentorship, or agility are shown." width="100%" height="100%" %}

### Our history

{{ site.org }} has evolved significantly since its inception in 2019. Initially conceived as an accessible resource for studying science subjects and practicing cooking skills, we quickly realised the value lay in the learning and networking opportunities during development. Our journey includes several key milestones:

- **2019**: Conceptualisation of Project27 as an accessible resource.
- **2021**: Collaboration with the MIT Visualisation Group, leading to new referrals for co-designing research projects in fields of accessible data visualisation, and self-advocacy.
- **2022**: Shift in focus to the active learning and mentorship process, leading to a refined value proposition.
- **March 2023**: Recognition at the London Business School with an innovation prize in the "investment-ready" category, for a research translation project under Project27 Solutions.
- **July 2023**: Registration as a Community Interest Company (CIC), uniting our community, research, and innovation services, to leverage synergies between the two business arms through creating additional development pathways for our community members as co-design consultants.

Currently, we are concentrating on developing the {{ site.brand }} value proposition, through stakeholder engagement, and aligning it with the resource needs and revenue streams associated with Project27 Solution activities.

{% include global/buttonLink.html url="/about/history.html" label="Find out more about where exactly our adventure began" %}

### Our founders

We are Daniel and Danielle, a couple from Brighton, England.
We wanted to learn, so we started developing {{ site.brand }}.
We live with disabilities, and we have a lot to share.

{% include global/buttonLink.html url="/about/team/index.html" label="Learn more about our team" %}

### Our services

We offer community services through our Project27 Skills portfolio, while our research and innovation services make up the Project27 Solutions portfolio.

{% assign home = site.data.main['Home'] %}
{% assign dataFile = home['services'] %}
{% include global/grid-generator-2.html heading="h4" %}