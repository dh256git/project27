{% assign skills = site.data.skills %}

{% capture text-skills %}
## Develop your skills with us

Our community has developed {{ skills | size }} unique skills to date, and counting!
Skillsets are a related group of skills that our trainees and volunteers can develop, associated with activities they engage in.
View the full set of skills we can support you with below.

{% assign skillsets = site.data.volunteering.skillsets %}
<div class="row">
<div class="col-3">
<p>Skillset:</p>
</div>
<div class="col-3">
<select onchange="handleChange2(this)">
{% for item in skillsets %}
<option value="{{ item.value | prepend: site.baseurl }}" label="{{ item.label }}">{{ item.text }}</option>
{% endfor %}
</select>
</div>

</div>

<div class="iframe-container">
<iframe src="{{ '/skills/accessibility.html' | prepend: site.baseurl }}" title="Accessibility skillset" id="iframe-id2" class="responsive-iframe"></iframe>
</div>
{% endcapture %}