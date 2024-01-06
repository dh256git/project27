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
You can contribute as a [volunteer,](#apply-to-volunteer-top) or as a [member,](#membership) and [develop your skills]({% link about/skills.md %}) through hands-on tasks.

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







### When can I become a volunteer?

Applications open on the 1st of October, 2023.
You can submit an application anytime after this date.

Volunteer registration will open with the launch of version 1.0 of the {{ site.brand }} site, on the 31st of January, 2024.

---





---

## What can I work on?

Browse our activity catalogue, and get involved.
Select a team, before viewing a list of available activities.
The activity pages provide an overview of what's expected, as well as a list of very specific tasks to choose from.

{% assign community-teams = site.data.volunteering.community %}
<div class="row">
<div class="col-3">
<p>Team:</p>
</div>
<div class="col-3">
<select onchange="handleChange(this)">
{% for item in community-teams %}
<option value="{{ item.value | prepend: site.baseurl }}" label="{{ item.label }}">{{ item.text }}</option>
{% endfor %}
</select>
</div>
<div class="col-6">
<a data-toggle="collapse" href="#how-it-works" aria-expanded="false" aria-controls="how-it-works">How does it work?</a>
</div>
</div>

<div class="collapse" id="how-it-works">
<h3>How does it work?</h3>

At the moment, we do it all.
And we can't wait to find people who do some of our tasks much better than we do.
That's how {{ site.brand }} grows.
That's also how we build a community of peer support.

We don't have roles, we work on tasks.
As such, we adopted <a href="https://mentorphile.com/2019/03/05/fostering-apples-culture-of-accountability-the-dri/">Apple's Directly Responsible Individual (DRI) way of working.</a>
Everyone in the team is directly responsible for the task assigned to them.

Some tasks are permanent, just like washing up is.
Other tasks may disappear once they are done, just like you would post a letter only once.
When you become a volunteer, you can bid on tasks, using an internal system.
The rest is history.
</div>

<div class="iframe-container">
<iframe src="{{ '/volunteering/research-and-development/index.html' | prepend: site.baseurl }}" title="Research and Development" id="iframe-id" class="responsive-iframe"></iframe>
</div>

{% include spotlight.html %}

---

## Membership at {{ site.brand }} {#membership}


We plan to open a membership application on 1st of January, 2024.
Members will access additional benefits, based on a subscription.




### When can I become a member?

Please, express your interest in becoming a member, by using the button below.
The launch date of membership registration may change depending on your interest.

We plan to open membership registration with the launch of version 2.0 of the {{ site.brand }} site, on the 31st of January, 2025.

<a id="apply-to-volunteer-bottom" class="{{ page.buttonStyle }}" aria-disabled="false" href="{{ '/volunteering/become-a-volunteer.html' | prepend: site.baseurl }}">I'd like to become A member</a>

---
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