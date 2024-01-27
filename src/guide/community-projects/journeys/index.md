---
layout: project
title: Project Journeys
projectNumber: 1
author: Danielle Garratt
profile: /about/team/Danielle/index.html
message: Hey, my name is Danielle, and I enjoy playing video games. It's also really rewarding to be able to design and create my own video game. Do you want to try creating your own game? Check out my notes on how I started my journey.
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
---

{% capture tab1-content %}
{% include projects/journeys/blog/index.md %}
{% endcapture %}

{% capture tab2-content %}
{% include projects/journeys/notes/index.md %}
{% endcapture %}

{% capture tab3-content %}
{% include projects/journeys/team/index.md %}
{% endcapture %}

{% include projects/project-tabs.html tab1="Blog" tab2="Notes" tab3="Team" tabpanel1=tab1-content tabpanel2=tab2-content tabpanel3=tab3-content %}