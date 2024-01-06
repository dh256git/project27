{% capture text-teams %}
## Which teams can I work with?

Select a team before viewing a list of available activities and tasks.
Teams are the backbone of our community.

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
That's how {{ site.org }} grows.
That's also how we build a community of peer support.

We don't have roles, we work on tasks.
As such, we adopted <a href="https://mentorphile.com/2019/03/05/fostering-apples-culture-of-accountability-the-dri/">Apple's Directly Responsible Individual (DRI) way of working.</a>
Everyone in the team is directly responsible for the task assigned to them.

Some tasks are permanent, just like washing up is.
Other tasks may disappear once they are done, just like you would post a letter only once.
When you become a volunteer, you can bid on tasks, using an internal system.
The rest is history.
</div>

## What can I work on?

Browse our activity catalogue below, and get involved with the team you selected above.

<div class="iframe-container">
<iframe src="{{ '/volunteering/research-and-development/index.html' | prepend: site.baseurl }}" title="Research and Development" id="iframe-id" class="responsive-iframe"></iframe>
</div>

The activity pages provide an overview of what's expected, as well as a list of very specific tasks to choose from.
It's tasks you can bid for, and multiple tasks will make up your mini project.

{% include spotlight.html %}
{% endcapture %}
