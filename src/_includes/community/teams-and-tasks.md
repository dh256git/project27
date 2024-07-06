{% capture text-teams %}
## Select your team

When trainees join our community, they join a team led by a volunteer.
The team you want to join depends on your interests and motivations.
Team members work towards the same goals, defined by related team activities, with interns, scholars, and fellows learning from each other.
Select a team before viewing a list of team specific activities.

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
<div>
<h3>How do {{ site.org }} teams work?</h3>

Teams are the backbone of our community, where peer support is central.
We don't have roles, we work on tasks.
As such, we adopted <a href="https://mentorphile.com/2019/03/05/fostering-apples-culture-of-accountability-the-dri/">Apple's Directly Responsible Individual (DRI) way of working.</a>

Everyone in the team is directly responsible for the task assigned to them.
However, everyone has a mentor to learn from, and a mentee to support.
Scholars learn from fellows, while interns are guided by scholars.
When you become a team member, you can bid on tasks, using our internal system.
</div>
</div>

## Find an activity

Activity pages provide an overview of related tasks, requirements, and development outcomes.
You can bid for activity specific tasks, using your Trello account and our task board.

<div class="iframe-container">
<iframe src="{{ '/volunteering/research-and-development/index.html' | prepend: site.baseurl }}" title="Research and Development" id="iframe-id" class="responsive-iframe"></iframe>
</div>
{% endcapture %}