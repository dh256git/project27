---
layout: default
title: "Happy Jekylling!"
list: [1, 2, 3, 4]
---

# Embedding YouTube video 

Hello

<iframe width="560" height="315" src="https://www.youtube.com/embed/2yzHkGTnAe4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Loops

Hello

{% for item in page.list   reversed%}
{{ item }}
{% endfor %}