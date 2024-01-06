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
{% include community/members.md %}
{% include community/volunteers.md %}
{% include community/teams-and-tasks.md %}
{% include community/events.md %}

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamContent = site.volunteering | where:"team","Content" %}

## {{ page.title }}: {{ page.tagline }}

Get involved and become a part of our community.
You can contribute as a [volunteer,](#apply-to-volunteer-top) or as a [member,](#apply-to-volunteer-top) and [develop your skills]({% link about/skills.md %}) through hands-on tasks.

{% include global/cover-image.html image="volunteering-cover.jpg" alt="A drawn tree, with handprints as leaves on the branches." %}

<div role='tablist'>
  <button role='tab' id='tab-overview' aria-controls='tabpanel-overview' onClick="setTab('overview')">Overview</button>
  <button role='tab' id='tab-members' aria-controls='tabpanel-members' onClick="setTab('members')">Members</button>
  <button role='tab' id='tab-volunteers' aria-controls='tabpanel-volunteers' onClick="setTab('volunteers')">Volunteers</button>
  <button role='tab' id='tab-teams' aria-controls='tabpanel-teams' onClick="setTab('teams')">Teams and Tasks</button>
  <button role='tab' id='tab-events' aria-controls='tabpanel-events' onClick="setTab('events')">Events</button>
</div>

<div role='tabpanel' id='tabpanel-overview' aria-labelledby='tab-overview'>
  {{ text-overview | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-members' aria-labelledby='tab-members'>
  {{ text-members | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-volunteers' aria-labelledby='tab-volunteers'>
  {{ text-volunteers | markdownify }}
</div>
<div role='tabpanel' id='tabpanel-teams' aria-labelledby='tab-teams'>
  {{ text-teams | markdownify }}
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