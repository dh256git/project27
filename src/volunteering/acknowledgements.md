---
layout: default
title: Acknowledgements
---

## {{ page.title }}
Anyone who has ever volunteered to contribute to {{ site.brand }} is acknowledged on this page.

{% for item in site.data.volunteering.acknowledgements %}
### {{ item.name }}

{{ item.contribution }}
{% endfor %}