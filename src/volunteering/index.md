---
layout: default
title: Volunteering
tagline: Together we learn, together we grow
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-10-02
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamContent = site.volunteering | where:"team","Content" %}

## {{ page.title }}: {{ page.tagline }}

Get involved!
Volunteer to work with the {{ site.brand }} team, and learn through hands-on tasks.
By doing so, you will also teach those who want to learn, but are not yet ready to roll their sleaves up.

{% include global/cover-image.html image="volunteering-cover.jpg" alt="A drawn tree, with handprints as leaves on the branches." %}

<a class="{{ page.buttonStyle }}" aria-disabled="false" href="{{ '/volunteering/become-a-volunteer.html' | prepend: site.baseurl }}">BECOME A VOLUNTEER</a>

---

## Volunteering opportunities

We do it all.
And we can't wait to find people who do some of our tasks much better than we do.
We don't have roles, we work on tasks.
As such, we adopted [Apple's Directly Responsible Individual (DRI) way of working.](https://mentorphile.com/2019/03/05/fostering-apples-culture-of-accountability-the-dri/)
Everyone in the team is directly responsible for the task assigned to them.

Still interested in volunteering?
We are ready to delegate.
The following tasks are waiting for you to take.

### Research and Development team

Join the Research and Development (R&D) team.
There are {{ teamRnD | size }} available tasks.
The R&D team members help with the research and development activities of {{ site.brand }}, such as website development or researching solutions to ongoing challenges in the project.

{% for member in teamRnD %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View details: {{ member.task }}</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}

### Content team

Join the Content team.
There are {{ teamContent | size }} available tasks.
The Content team helps with authoring new notes for {{ site.product }}.

{% for member in teamContent %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View details: {{ member.task }}</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}

### Editorial and review team

Join the Editorial and Review team.
There are {{ teamER | size }} available tasks.
The team of editors and reviewers help us make sure content is relevant and a high quality.

{% for member in teamER %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View details: {{ member.task }}</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}

### Management team

Join the management team.
 We need to plan the future, while coordinating our work in the present.
There are {{ teamLeadership | size }} available tasks.
Members of the management team help with business activities and other key tasks.
Managers lead by example, supporting volunteers of other teams.
Team members can break down  their tasks, and recruit new members to work on these smaller tasks.
By doing so, they can also create new, senior leadership roles in the C-suite of {{ site.brand }} for themselves.

{% for member in teamLeadership %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View details: {{ member.task }}</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}

---

## Why would I volunteer to contribute to {{ site.brand }}?

**Do it for yourself.**

<ol>
<li>
Learn new skills, or improve your existing skills.<div id="volunteer1"></div><div id="morevolunteer1">
{{ site.brand }} is all about learning new skills, and getting better in doing certain things, by practicing, and innovating.
The project offers a wide range of skills to pick up and nurture, and you get to choose which is most valuable to you.All that {{ site.brand }} volunteering roles do, is setting SMART (Specific, Measurable, Achievable, Relevant, and Timely) targets for you to work towards.
</div>
<button onclick="readMoreVolunteering1()" id= "Read-More-BTN1">Read more</button>
</li>

<li>
Use your knowledge and productivity output to help others.<div id= "volunteer2"></div><div id="morevolunteer2">
In the process of learning, you are also contributing to a shared vision.
You could learn on your own, and practice through your personal project.
Wouldn't it be more satisfying though, to help other people in the process?
There are no deadlines, no punishment if something doesn't work out.
It's learning through trial and error, and practice.
</div>
<button onclick="readMoreVolunteering2()" id="Read-More-BTN2">Read more</button>
</li>

<li>
Be part of a team. <div id= "volunteer3"></div><div id="morevolunteer3">
 Vibrant teams maintain a friendly vibe.
 There will be opportunities to be social by both digital and physical ways.
 Turn up for every, or every fifth team checkin.
 Stay for an hour, or drop in for only ten minutes.
 Being socially proactive is not a must, only an opportunity.
</div>
<button onclick="readMoreVolunteering3()" id="Read-More-BTN3">Read more</button>
</li>

<li>
Satisfy your dopamine with an extra reward. <div id= "volunteer4"></div> <div id="morevolunteer4">
Are you the collector type, gathering and displaying credits, kudos,, acknowledgements, thanks, and all that jazz?

Then you'll also get the rewards on <a href="/about/team/index.html">our team page,</a> as well as in the inner circle of {{ site.brand }}.
</div>
<button onclick="readMoreVolunteering4()" id="Read-More-BTN4">Read more</button>
</li>
</ol>

---

## How much time should you commit?

The level of engagement is flexible. You may

+ identify, or ask me for a single challenge, solve it, and you are done.
+ continue working on multiple challenges, whenever you find time, even if only a couple hours in a month.
+ get hooked, and if you have nothing better to do, treat it as a part time role.

---

## Become a {{ site.brand }} volunteer

Are you interested in contributing to {{ site.brand }} and becoming a volunteer?
Please, express your interest by using the button below.

<!--Note: Decide best method of expressing interest.-->

