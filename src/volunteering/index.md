---
layout: default
title: Community
tagline: Together we learn, together we grow
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-10-02
licence: copyright
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% include community/overview.md %}
{% include community/trainees.md %}
{% include community/volunteers.md %}
{% include community/teams-and-tasks.md %}
{% include community/skills.md %}
{% include community/events.md %}


{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamContent = site.volunteering | where:"team","Content" %}

## {{ page.title }}: {{ page.tagline }}

{% include global/buttonLink.html url="https://docs.google.com/forms/d/e/1FAIpQLSeq5EFjDtIjXKPDgu8l9YYBwfP7gnrop7uKOTRoIxtZZQTRwQ/viewform?usp=sf_link" label="Express your interest in joining our community" %}

Join our community as a 
<a href="#tab-volunteers" onClick="setTab('volunteers')">
volunteer,
</a>
 or as a 
 <a href="#tab-trainees" onClick="setTab('trainees')">
trainee.
</a>
The trainee programme helps blind or learning disabled people to learn through peer support and mentoring.
Anyone can volunteer, as long as they are joining us to support trainees through their professional experience. 
Our members, volunteers and trainees alike, come to 
<a href="#tab-skills" onClick="setTab('skills')">
develop skills that matter,
</a>
 through bespoke training, creating and completing tasks, and working in disability inclusive teams.

{% include global/cover-image.html image="volunteering-cover.jpg" alt="A drawn tree, with handprints as leaves on the branches." %}

## Book a support session

Membership is not required to get support from us.
We offer bookable, paid support sessions for anyone who wants to get advice on topics related to blindness or learning disability.
The first session is free for everyone, creating an opportunity for introductions and an assessment of your support needs.

{% include global/buttonLink.html url="/support/index.html" label="View our ad hoc support offer" %}

<div role='tablist'>
  <button role='tab' id='tab-overview' aria-controls='tabpanel-overview' onClick="setTab('overview')">Overview</button>
  <button role='tab' id='tab-trainees' aria-controls='tabpanel-trainees' onClick="setTab('trainees')">Trainees</button>
  <button role='tab' id='tab-volunteers' aria-controls='tabpanel-volunteers' onClick="setTab('volunteers')">Volunteers</button>
  <button role='tab' id='tab-teams' aria-controls='tabpanel-teams' onClick="setTab('teams')">Teams and Tasks</button>
  <button role='tab' id='tab-skills' aria-controls='tabpanel-skills' onClick="setTab('skills')">Skills</button>
  <button role='tab' id='tab-events' aria-controls='tabpanel-events' onClick="setTab('events')">Events</button>
</div>

<div role='tabpanel' id='tabpanel-overview' aria-labelledby='tab-overview'>
  {{ text-overview | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-trainees' aria-labelledby='tab-trainees'>
  {{ text-trainees | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-volunteers' aria-labelledby='tab-volunteers'>
  {{ text-volunteers | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-teams' aria-labelledby='tab-teams'>
  {{ text-teams | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-skills' aria-labelledby='tab-skills'>
  {{ text-skills | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-events' aria-labelledby='tab-events'>
  {{ text-events | markdownify }}
</div>

<script>

  setTab('overview');

  function setTab(tabName) {
    console.log(tabName);
    const allTabButtons = document.querySelectorAll('button[role=tab]');

    const tabButtonId = 'tab-' + tabName;
    const selectedTabButton = document.getElementById(tabButtonId);

    allTabButtons.forEach((tabButton) => {
      tabButton.setAttribute('aria-selected', false);
    });
    selectedTabButton.setAttribute('aria-selected', true);

    const allTabPanels = document.querySelectorAll('[role=tabpanel]');

    const tabPanelId = 'tabpanel-' + tabName;
    const selectedTabPanel = document.getElementById(tabPanelId);

    allTabPanels.forEach((tabPanel) => {
      tabPanel.setAttribute('hidden', true);
    });
    selectedTabPanel.removeAttribute('hidden');

    console.log(tabName, selectedTabButton, selectedTabPanel)
  }
</script>