---
layout: default
title: Meet the team
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
listOfIcons: [["", ""], ["", ""]]
---

## {{ page.title }}

Anyone who has ever volunteered to contribute to {{ site.brand }} is acknowledged on this page.
Find out more about the people who make up the team.

{% for item in site.data.volunteering.team %}
### {{ item.name }} - {{ site.brand }} {{ item.role }}

<img src="{{ item.photo | prepend: site.baseurl }}" alt="{{ item.alt }}" height="400px" width="300px">

{{ item.contribution }}

[View {{ item.shortname }}'s profile]({{ item.profile | prepend: site.baseurl }})
{% endfor %}