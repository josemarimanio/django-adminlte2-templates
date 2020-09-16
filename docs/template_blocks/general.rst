.. template_blocks/general


=======
General
=======


<html> content
--------------

.. data:: html_attribute
    :noindex:

    HTML ``<html>`` attributes.

    Default:

    .. code:: jinja

        <html {% block html_attribute %}lang="{% block html_lang %}{{ ADMINLTE_HTML_LANG }}{% endblock html_lang %}" dir="{% block html_lang_bidi %}{{ ADMINLTE_HTML_LANG_BIDI }}{% endblock html_lang_bidi %}" {% endblock html_attribute %}>


.. data:: html_lang
    :noindex:

    HTML ``<html>`` ``lang`` attribute.

    Default:

    .. code:: jinja

        lang="{% block html_lang %}{{ ADMINLTE_HTML_LANG }}{% endblock html_lang %}"


.. data:: html_lang_bidi
    :noindex:

    HTML ``<html>`` ``dir`` attribute

    Default:

    .. code:: jinja

        dir="{% block html_lang_bidi %}{{ ADMINLTE_HTML_LANG_BIDI }}{% endblock html_lang_bidi %}"


<head> content
--------------

.. data:: extra_head
    :noindex:

    Additional HTML tags in ``<head>``.


.. data:: meta
    :noindex:

    ``<meta>`` tags in ``<head>``.

    Default:

    .. code:: jinja

        {% block meta %}
            {% include 'adminlte2/components/_meta.html' %}
        {% endblock meta %}


.. data:: title
    :noindex:

    HTML ``<title>`` tag text.


.. data:: stylesheets
    :noindex:

    CSS links in ``<head>``.

    Default:

    .. code:: jinja

        {% block stylesheets %}
            {% include 'adminlte2/components/_stylesheets.html' %}
        {% endblock stylesheets %}


.. data:: stylesheets_fix
    :noindex:

    Custom CSS links in ``<head>``. Included custom CSS files are:

    - ``adminlte2/fix/header_dropdown_link_color.css``: Custom CSS to fix header dropdown link color without using ``.notifications-menu``, ``.messages-menu``, or ``.tasks-menu`` classes

    Default:

    .. code:: jinja

        {% block stylesheets_fix %}
            {% include 'adminlte2/components/_stylesheets_fix.html' %}
        {% endblock stylesheets_fix %}


.. data:: favicon
    :noindex:

    Favicon links in ``<head>``:

    Default:

    .. code:: jinja

        {% block favicon %}
            <link rel="shortcut icon" href="{% block favicon_icon %}{% static 'favicon.ico' %}{% endblock favicon_icon %}">
        {% endblock favicon %}


.. data:: favicon_image
    :noindex:

    Favicon image path.

    Default:

    .. code:: jinja

        <link rel="shortcut icon" href="{% block favicon_icon %}{% static 'favicon.ico' %}{% endblock favicon_icon %}">


.. data:: shim
    :noindex:

    HTML 5 Shim JavaScript links in ``<head>``.

    Default:

    .. code:: jinja

        {% block shim %}
            {% if ADMINLTE_USE_SHIM %}
                {% include 'adminlte2/components/_shim.html' %}
            {% endif %}
        {% endblock shim %}


.. data:: javascripts
    :noindex:

    JavaScript links in ``<head>``.

    Default:

    .. code:: jinja

        {% block javascripts %}
            {% include 'adminlte2/components/_javascripts.html' %}
        {% endblock javascripts %}


<body> content
--------------

.. data:: body
    :noindex:

    HTML ``<body>`` tag content.


.. data:: body_attribute
    :noindex:

    HTML ``<body>`` attributes.

    Default:

    .. code:: jinja

        <body {% block body_attribute %}class="{% block body_class %}hold-transition {% block skin_style %}{{ ADMINLTE_SKIN_STYLE }}{% endblock skin_style %}{% endblock body_class %}"{% endblock body_attribute %}>


.. data:: body_class
    :noindex:

    HTML ``<body>`` tag ``class`` attributes.

    Default:

    .. code:: jinja

        {% block body_class %}hold-transition {{ ADMINLTE_SKIN_STYLE }}{% endblock body_class %}


.. data:: skin_style
    :noindex:

    HTML ``<body>`` tag ``class`` attribute for AdminLTE 2 skin theme.

    Valid values are: ``'skin-black'``, ``'skin-black-light'``, ``'skin-blue'``, ``'skin-blue-light'``,
    ``'skin-green'``, ``'skin-green-light'``, ``'skin-purple'``, ``'skin-purple-light'``,
    ``'skin-red'``, ``'skin-red-light'``, ``'skin-yellow'``, ``'skin-yellow-light'``.


.. data:: javascripts_body
    :noindex:

    JavaScript links in ``<body>``.
