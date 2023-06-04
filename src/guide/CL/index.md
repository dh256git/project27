---
layout: default
title: Digital skills
levelToOpen: chapter
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
listOfIcons: [["", "Bash shell logo.png"], ["", "Github logo.png"], ["", "Markdown logo.png"], ["", "Jekyll logo.png"], ["", "Python logo.png"], ["", "Rlogo.png"]]
---

{% comment %}
<div class="container">
{% endcomment %}

## {{ page.title }}

This volume includes notes on developing useful digital skills, and learning how to use tools, such as the command-line, git version control, or web technologies.

Initially, we include four chapters in this volume.
These topics cover technologies and digital skills we learnt, while building the {{ site.brand }} site.

---

{% assign dataFile = site.data.chapters.CL %}
{% assign gridLimit = 4 %}
{% include global/grid-generator.html heading="h3" %}

{% comment %}
</div>
{% endcomment %}