---
layout: default
title: Dashboard
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
listOfIcons: [["", ""], ["", ""]]
burndownData: /about/dashboard/burndown-data/sprint01.csv
---
# {{ page.title }}

Welcome to the project dashboard.
View status updates below.

{% include dashboard/burndown.html %}