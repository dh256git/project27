---
layout: default
title: Volunteering and contributionsReview", "Content 
buttonStyle: mybtn
---

{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamCC = site.volunteering | where:"team","CC" %}

## Call for volunteers and contributors

**Come and help {{ site.brand }}, and {{ site.brand }} will help you.**

> If you'd like to volunteer your time, and learn a new skill, or improve and existing skill you have and I don't, then please consider helping me.

Daniel - {{ site.brand }} editor

---

## Volunteering opportunities

The following tasks are waiting for you to take.

### Research and Development team

Join the Research and Development (R&D) team.
There are {{ teamRnD | size }} available tasks.
The R&D team members help with the research and development activities of {{ site.brand }}, such as website development or researching solutions to ongoing challenges in the project.

{% for member in teamRnD %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
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

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}

### Content Creation team

Join the Content Creation team.
There are {{ teamCC | size }} available tasks.
The Content Creation team helps with authoring new notes for {{ site.product }}.

{% for member in teamCC %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">View task details</a>
{% else %}
<p>Currently no roles are available in this team.</p>
{% endfor %}

---

## Why would I volunteer to contribute to {{ site.brand }}?

**Do it for yourself.**

{% capture benefit1 %}
{{ site.brand }} is all about learning new skills, and getting better in doing certain things, by practicing, and innovating.
The project offers a wide range of skills to pick up and nurture, and you get to choose which is most valuable to you.
All that {{ site.brand }} volunteering roles do, is setting SMART (Specific, Measurable, Achievable, Relevant, and Timely) targets for you to work towards.
{% endcapture %}

{% capture benefit2 %}
In the process of learning, you are also contributing to a shared vision.
You could learn on your own, and practice through your personal project.
Wouldn't it be more satisfying though, to help other people in the process?
There are no deadlines, no punishment if something doesn't work out.
It's learning through trial and error, and practice.
{% endcapture %}

{% capture benefit3 %}
 Vibrant teams maintain a friendly vibe.
 There will be opportunities to be social by both digital and physical ways.
 Turn up for every, or every fifth team checkin.
 Stay for an hour, or drop in for only ten minutes.
 Being socially proactive is not a must, only an opportunity.
{% endcapture %}

{% capture benefit4 %}
Are you the collector type, gathering and displaying credits, kudos,, acknowledgements, thanks, and all that jazz?
Then you'll also get the rewards on the <a href="./acknowledgements.html">public acknowledgements page,</a> as well as in the inner circle of {{ site.brand }}.
{% endcapture %}

{% include global/collapseable.html trigger="Learn new skills, or improve your existing skills." paragraph=benefit1 ID="b01" %}
{% include global/collapseable.html trigger="Use your knowledge and productivity output to help others." paragraph=benefit2 ID="b02" %}
{% include global/collapseable.html trigger="Be part of a team." paragraph=benefit3 ID="b03" %}
{% include global/collapseable.html trigger="Satisfy your dopamine needs with an extra reward." paragraph=benefit4 ID="b04" %}

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

<button class="mybtn" aria-disabled="true" href="#">
BECOME A VOLUNTEER
</button>