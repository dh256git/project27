---
layout: default
title: Project27 Skills
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

Developing {{ site.brand }} is an extensive source of learning and enjoyment.
There are a range of topics that matter to us in the team.
We use these topics to facilitate the development of our own skills, while building the {{ site.brand }} {{ site.product }}.
As a result, we get better at doing things, and record an ever growing list of skills that matter to us.
If you find a skill on the list that matters to you too, and you want to learn by getting involved, please [check out our volunteer opportunities.]({% link volunteering/index.md %})

### Skills that matter to us: {{ skills | size }} and counting

So far, we have been on the journey of learning {{ skills | size }} skills. We are expanding this list as we go.

#### Accessibility

<ul>
{% for item in skills %}
{% if item.Category == 'Accessibility' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Web development

<ul>
{% for item in skills %}
{% if item.Category == 'Web development' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Digital skills

<ul>
{% for item in skills %}
{% if item.Category == 'Digital skills' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Entrepreneurship

<ul>
{% for item in skills %}
{% if item.Category == 'Entrepreneurship' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Social skills

<ul>
{% for item in skills %}
{% if item.Category == 'Social skills' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Personal competencies

<ul>
{% for item in skills %}
{% if item.Category == 'Personal competencies' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Journalism

<ul>
{% for item in skills %}
{% if item.Category == 'Journalism' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Research

<ul>
{% for item in skills %}
{% if item.Category == 'Research' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

---

### Skills that matter to you

If the {{ site.brand }} {{ site.product }} does not include a topic you are interested in, and the skills that matter to us exclude the skills you want to develop, we may still be able to support you.

We are committed to host and showcase your very own project on our community platform.
The platform allows you to write your own project blog, organise your resources and content, recruit contributors, as well as offer your support within your project community.

To find out more, contact us:

- via e-mail: support@project27skills.com.