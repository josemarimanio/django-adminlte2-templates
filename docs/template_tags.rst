=============
Template Tags
=============

**django-adminlte2-templates** template tags can be used by adding ``{% load adminlte2_tags %}`` to the template:


.. data:: {% add_active %}
    :noindex:

    Add ``' active '`` class to sidebar and header navigation links based on comparison of URL pattern with current URL.

    Parameters:

    - ``url_pattern``: *(str)* URL pattern for ``reverse`` matching

    - ``exact_match``: *(bool, optional)* Toggle for exact matching, defaults to ``False``

    - ``not_when``: *(str, optional)* Comma-separated string of patterns that will render comparison as False, defaults to ``''``

    - ``*args`` and ``**kwargs`` for URL ``reverse`` matching

    Example:

    .. code:: jinja

        <li class="{% add_active 'app:page' object.pk %}">
            <a href="{% url 'app:page' object.pk %}">Details</a>
        </li>
