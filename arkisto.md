---
title: Arkisto
permalink: /arkisto/
---

# Arkisto

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
