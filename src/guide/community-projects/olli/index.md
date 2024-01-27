---
layout: project
title: Project Olli
projectNumber: 0
author: Daniel Hajas
profile: /about/team/Daniel/index.html
message: Hi, I'm daniel, and Olli is one of my community projects. If screen reader accessibility of data visualisations on the web matters to you, please consider joining the team of collaborators behind Olli. To find out more, click on the "team" tab.
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
listOfIcons: [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
---

{% capture tab1-content %}
{% include projects/olli/blog/index.md %}
{% endcapture %}

{% capture tab2-content %}
{% include projects/olli/notes/index.md %}
{% endcapture %}

{% capture tab3-content %}
{% include projects/olli/team/index.md %}
{% endcapture %}

{% include projects/project-tabs.html tab1="Blog" tab2="Notes" tab3="Team" tabpanel1=tab1-content tabpanel2=tab2-content tabpanel3=tab3-content %}