---
layout: default
title: Who we are?
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
listOfIcons: [["", ""], ["", ""]]
---

<h2>{{ page.title }}</h2>

We are a small but committed social enterprise with great friends and advisors.
View who is in our core team, who gives us advice, and who are our community members.

### The core team

{{ site.org }} is managed by this awesome core team.

{% assign teamMembers = site.data.volunteering.core-team %}
{% include team/profile-preview.html %}

---

### The advisory team

We wouldn't be where we are today, without the invaluable advice and guidance of our advisors.

{% assign teamMembers = site.data.volunteering.advisory-team %}
{% include team/profile-preview.html %}

---

### The volunteer and trainee team

Say hello to our community members. These are the people we exist for.

{% assign teamMembers = site.data.volunteering.volunteer-team %}
{% include team/profile-preview.html %}