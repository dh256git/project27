---
layout: default
title: Dashboard
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
listOfIcons: [["", ""], ["", ""]]
burndownData: /about/dashboard/burndown-data/current-sprint.csv
---
# {{ page.title }}

Welcome to the project dashboard.
View status updates below. Currently, the burndown chart is not accessible on mobile platforms.

{% include dashboard/burndown.html %}