=========================
Template Tags and Filters
=========================

**django-adminlte2-templates** provides several template tags and filters that can be used by adding ``{% load adminlte2_tags %}`` to your layout templates:


Tags
----

.. data:: {% add_active %}
    :noindex:

    Add HTML class name ``active`` to sidebar and header navigation links based on comparison of given URL pattern with current URL.

    **Parameters**:

    **url_pattern**:
        *(str)* URL pattern for ``reverse`` matching.

    **exact_match**:
        *(bool, optional)* Toggle for exact matching, defaults to ``False``.

    **not_when**:
        *(str, optional)* Comma-separated string of patterns that will render comparison as ``False``, defaults to ``''``.

    **\*args** and **\*\*kwargs**
        For URL ``reverse`` matching.

    Example:

    .. code:: jinja

        <li class="{% add_active 'app:page' object.pk %}">
            <a href="{% url 'app:page' object.pk %}">Details</a>
        </li>


.. data:: {% gravatar_url %}
    :noindex:

    Generates a `Gravatar URL <https://en.gravatar.com/support/what-is-gravatar/>`_  based on the details of the current user.

    For your convenience, you can also set the parameters related to this tag in Django ``settings.py``. Please check the `Settings <settings.html>`_ > `Gravatar <settings.html#gravatar>`_ section for more information.

    To know more about Gravatar request parameters, please check the `Gravatar Image Request documentation <https://en.gravatar.com/site/implement/images/>`_ for more information.

    **Parameters**:

    **user**:
        *(User object, optional)* User object, defaults to context ``user``.

    **size**:
        *(int, optional)* Image size. You may request images anywhere from ``1`` up to ``2048``, however note that many users have lower resolution images, so requesting larger sizes may result in pixelation/low-quality images. Defaults to ``80``.

    **default**:
        *(str, optional)* Default Gravatar image to load. You can supply your own default image by supplying the URL to an image.
        Alternatively, you can use any of these valid values: ``'404'``, ``'mp'``, ``'identicon'``, ``'monsterid'``, ``'wavatar'``, ``'retro'``, ``'robohash'``, ``'blank'``. Defaults to ``'mp'``.

    **force_default**:
        *(bool, optional)* Toggle to force load default Gravatar image, defaults to ``False``.

    **rating**:
        *(str, optional)* Gravatar image rating. Valid values are: ``'g'``, ``'pg'``, ``'r'``, ``'x'``. Defaults to ``'pg'``.

    Example:

    .. code:: jinja

        <img src="{% gravatar_url %}" alt="User Avatar">


.. data:: {% paginator %}
    :noindex:

    Generates an HTML code block for ListView pagination. HTML code output is based on template layout ``adminlte2/extras/paginator.html``.

    You can customize the output by overriding the aforementioned layout and using the template blocks related to this tag.
    Please check the `Template Blocks <template_blocks.html>`_ > `Paginator <template_blocks.html#paginator>`_ section for more information.

    **Parameters**:

    **adjacent_pages**
        *(int, optional)* Adjacent page links to current page link, defaults to ``2``.

    **align**
        *(str, optional)* Element alignment. Valid values are ``'initial'``, ``'center'``, ``'left'``, ``'right'``, defaults to ``'initial'``.

    **no_margin**
        *(bool, optional)* Toggle to remove margin around element, defaults to ``False``.

    Example:

    .. code:: jinja

        {% if is_paginated %}
            {% paginator adjacent_pages=2 align="center" no_margin=True %}
        {% endif %}


.. data:: {% page_title %}
    :noindex:

    Generates text for HTML <title> tag. Supports Django ``sites`` framework and ``ListView`` pagination.

    You can customize the output by using the settings related to this tag in Django ``settings.py``. Please check the `Settings <settings.html>`_ > `Page Title <settings.html#page-title>`_ section for more information.

    **Parameters**:

    **page_name**
        *(str, optional)* Page title text. Adding ``page_name`` to the page context will override this parameter. Defaults to ``''``.

    Example:

    .. code:: jinja

        {% block title %}{% page_title 'Page Title' %}{% endblock title %}


Filters
-------

.. data:: add_class
    :noindex:

    Add HTML class names to a form field.

    Example:

    .. code:: jinja

        {% for field in form %}
            <div class="form-group {% if field.errors %}has-error{% endif %}">
                {{ field.label_tag }}
                {% if field.errors %}
                    <div class="text-danger">
                        {{ field.errors }}
                    </div>
                {% endif %}
                {{ field|add_class:'form-control' }}
                {% if field.help_text %}
                    <p class="help-block">{{ field.help_text|safe }}</p>
                {% endif %}
            </div>
        {% endfor %}
