{% capture text-teams %}
## Which teams can I work with?

Teams are the backbone of our community.
When you first join {{ site.org }}, you join a team.
Which team you want to join depends on your interests and motivations.
Team members work towards the same goals; with trainees, interns, and fellows learning from each other.
<a data-toggle="collapse" href="#how-it-works" aria-expanded="false" aria-controls="how-it-works">Read more...</a>

Select a team before viewing a list of available activities and tasks.

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
<div class="collapse" id="how-it-works">
<h3>How do {{ site.org }} teams work?</h3>

Building teams  is the way we build a community, where peer support is central.
We don't have roles, we work on tasks.
As such, we adopted <a href="https://mentorphile.com/2019/03/05/fostering-apples-culture-of-accountability-the-dri/">Apple's Directly Responsible Individual (DRI) way of working.</a>

Everyone in the team is directly responsible for the task assigned to them.
However, everyone has a mentor to learn from, and a mentee to support.
Interns learn from fellows, while trainees are guided by interns.
When you become a team member, you can bid on tasks, using our internal system.
</div>
</div>
</div>

## What can I work on?

Browse our activity catalogue below, and get involved with the team you selected above.
The activity pages provide an overview of related tasks and outcomes.
You can bid for specific tasks in an activity, using your Trello account and our task board.

<div class="iframe-container">
<iframe src="{{ '/volunteering/research-and-development/index.html' | prepend: site.baseurl }}" title="Research and Development" id="iframe-id" class="responsive-iframe"></iframe>
</div>

{% include spotlight.html %}
{% endcapture %}
