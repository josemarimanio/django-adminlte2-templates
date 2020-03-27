===============
Template Blocks
===============


General
-------

General template tags:

<head> content
^^^^^^^^^^^^^^

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
            {% include 'adminlte2/components/_stylesheets/bootstrap.html' %}
            {% include 'adminlte2/components/_stylesheets/fontawesome.html' %}
            {% include 'adminlte2/components/_stylesheets/adminlte.html' %}
        {% endblock stylesheets %}


.. data:: javascripts
    :noindex:

    JavaScript links in ``<head>``.

    Default:

    .. code:: jinja

        {% block javascripts %}
            {% include 'adminlte2/components/_javascripts/jquery.html' %}
            {% include 'adminlte2/components/_javascripts/bootstrap.html' %}
            {% include 'adminlte2/components/_javascripts/adminlte.html' %}
        {% endblock javascripts %}


<body> content
^^^^^^^^^^^^^^

.. data:: body
    :noindex:

    HTML ``<body>`` tag content.


.. data:: body_class
    :noindex:

    HTML ``<body>`` tag ``class`` attributes.

    Default:

    .. code:: jinja

        {% block body_class %}hold-transition {{ ADMINLTE_SKIN_STYLE }}{% endblock body_class %}


Layouts
-------

*Sidebar* and *top navigation* layout template tags:


Templates
^^^^^^^^^

.. data:: header_template
    :noindex:

    AdminLTE 2 navigation header template.

    Default:

    .. code:: jinja

        {% block header_template %}
            {% include 'adminlte2/components/header.html' %}
        {% endblock header_template %}


.. data:: sidebar_template
    :noindex:

    AdminLTE 2 navigation sidebar template.

    Default:

    .. code:: jinja

        {% block sidebar_template %}
            {% include 'adminlte2/components/sidebar.html' %}
        {% endblock sidebar_template %}


.. data:: messages_template

    Django ``messages`` alert box template.

    Default:

    .. code:: jinja

        {% block messages_template %}
            {% include 'adminlte2/components/messages.html' %}
        {% endblock messages_template %}


.. data:: control_template

    AdminLTE 2 control sidebar template.

    Default:

    .. code:: jinja

        {% block control_sidebar %}
            {% include 'adminlte2/components/control.html %}
        {% endblock control_sidebar %}


.. data:: footer_template

    AdminLTE 2 footer template.

    Default:

    .. code:: jinja

        {% block footer_template %}
            {% include 'adminlte2/components/footer.html' %}
        {% endblock footer_template %}


Content
^^^^^^^

.. data:: content_template
    :noindex:

    AdminLTE 2 page content code.

    Default:

    .. code:: jinja

        {% block content_template %}
                <div class="content-wrapper">

                    <div class="container">

                        {% block content_header %}
                            <section class="content-header">
                                <h1>
                                    {% block page_title %}{% endblock page_title %}
                                    <small>{% block page_description %}{% endblock page_description %}</small>
                                </h1>
                                <ol class="breadcrumb">
                                    {% block breadcrumbs %}{% endblock breadcrumbs %}
                                </ol>
                            </section>
                        {% endblock content_header %}

                        {% block content_body %}
                            <section class="content">
                                {% block messages_template %}
                                    {% include 'adminlte2/components/messages.html' %}
                                {% endblock messages_template %}

                                {% block content %}
                                {% endblock content %}
                            </section>
                        {% endblock content_body %}
                    </div>
                </div>
            {% endblock content_template %}


.. data:: content_header
    :noindex:

    Page content header code.

    Default:

    .. code:: jinja

        {% block content_header %}
            <section class="content-header">
                <h1>
                    {% block page_title %}{% endblock page_title %}
                    <small>{% block page_description %}{% endblock page_description %}</small>
                </h1>

                <ol class="breadcrumb">
                    {% block breadcrumbs %}{% endblock breadcrumbs %}
                </ol>
            </section>
        {% endblock content_header %}


.. data:: page_title
    :noindex:

    Page title text that will be displayed in the content header.


.. data:: page_description
    :noindex:

    Page description text that will be displayed in the content header.


.. data:: breadcrumbs
    :noindex:

    Breadcrumb navigation that will be displayed in the content header.


.. data:: content
    :noindex:

    Page main content.


Header
^^^^^^

django-adminlte2-templates supports header for both  **sidebar** (*boxed, collapsed, fixed*) and
**top navigation** layouts:

.. data:: logo
    :noindex:

    Header logo code.

    Default for *sidebar*:

    .. code:: jinja

        {% block logo %}
            <a href="{% block logo_href %}/{% endblock %}" class="logo">
                <span class="logo-mini">{% block logo_mini %}<b>A</b>LTE{% endblock logo_mini %}</span>
                <span class="logo-lg">{% block logo_lg %}<b>Admin</b>LTE{% endblock logo_lg %}</span>
            </a>
        {% endblock logo %}

    Default for *top navigation*:

    .. code:: jinja

        {% block logo %}
            <a href="{% block logo_href %}/{% endblock logo_href %}" class="navbar-brand">
                {% block logo_lg %}
                    <b>Admin</b>LTE
                {% endblock logo_lg %}
            </a>
        {% endblock logo %}


.. data:: logo_href
    :noindex:

    Header logo link URL.


.. data:: logo_mini
    :noindex:

    (*sidebar* only) Header logo content when the *sidebar* content is collapsed.

    Default:

    .. code:: html

        <b>A</b>LTE


.. data:: logo_lg
    :noindex:

    Header logo content when *sidebar* content is exposed, or for *top navigation* layout.

    Default:

    .. code:: html

        <b>Admin</b>LTE


.. data:: header_content
    :noindex:

    Header main content code.

    Default for *sidebar*:

    .. code:: jinja

        {% block header_content %}
            <nav class="navbar navbar-static-top">
                {% block sidebar_toggle %}
                    <a href="#" class="sidebar-toggle" data-toggle="offcanvas" role="button">
                        <span class="sr-only">
                            {% block sidebar_toggle_text %}Toggle navigation{% endblock sidebar_toggle_text %}
                        </span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                {% endblock sidebar_toggle %}

                <div class="navbar-custom-menu">
                    <ul class="nav navbar-nav">
                        {% block header_items %}
                        {% endblock header_items %}
                    </ul>
                </div>
            </nav>
        {% endblock header_content %}

    Default for *top navigation*:

    .. code:: jinja

        {% block header_content %}
            <div class="collapse navbar-collapse pull-left" id="navbar-collapse">
                <ul class="nav navbar-nav">
                    {% block header_items_left %}
                    {% endblock header_items_left %}
                </ul>
            </div>

            <div class="navbar-custom-menu">
                <ul class="nav navbar-nav">
                    {% block header_items %}
                        {% block header_items_right %}
                        {% endblock header_items_right %}
                    {% endblock header_items %}
                </ul>
            </div>
        {% endblock header_content %}


.. data:: header_items
    :noindex:

    Header (right) navigation items.


.. data:: header_items_left
    :noindex:

    (*top navigation* only) Header left navigation items.


.. data:: header_items_right
    :noindex:

    (*top navigation* only) Header right navigation items. Alias for ``header_items``.

    Default:

    .. code:: jinja

        {% block header_items %}
            {% block header_items_right %}
            {% endblock header_items_right %}
        {% endblock header_items %}


.. data:: sidebar_toggle
    :noindex:

    (*sidebar* only) Sidebar toggle button for sidebar (*boxed, collapsed, fixed*) layouts.

    Default:

    .. code:: jinja

        {% block sidebar_toggle %}
            <a href="#" class="sidebar-toggle" data-toggle="offcanvas" role="button">
                <span class="sr-only">
                    {% block sidebar_toggle_text %}Toggle navigation{% endblock sidebar_toggle_text %}
                </span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </a>
        {% endblock sidebar_toggle %}


.. data:: sidebar_toggle_text
    :noindex:

    (*sidebar* only) Sidebar toggle button screenreader text for sidebar (*boxed, collapsed, fixed*) layouts.

    Default::

        Toggle navigation


.. data:: header_toggle
    :noindex:

    (*top navigation* only) Responsive toggle button for left navigation links.

    Default:

    .. code:: jinja

        {% block header_toggle %}
            <button type="button" class="navbar-toggle collapsed"
                data-toggle="collapse" data-target="#navbar-collapse">
                <span class="sr-only">
                    {% block header_toggle_text %}Toggle navigation{% endblock header_toggle_text %}
                </span>
                <i class="fa fa-bars"></i>
            </button>
        {% endblock header_toggle %}


.. data:: header_toggle_text

    (*top navigation* only) Responsive toggle button screenreader text for left navigation links.

    Default::

        Toggle navigation


Sidebar
^^^^^^^

.. data:: sidebar_title
    :noindex:

    Sidebar navigation title text.

    Default::

        MAIN NAVIGATION


.. data:: sidebar_items
    :noindex:

    Sidebar navigation items.


Control
^^^^^^^

.. data:: control_items
    :noindex:

    Control sidebar navigation items.


.. data:: control_tabs
    :noindex:

    Control sidebar navigation tab contents.


Messages
^^^^^^^^

Django ``messages`` alert boxes.

.. data:: message_debug
    :noindex:

    ``DEBUG`` alert box.

    Default:

    .. code:: html

        <div class="alert alert-info alert-dismissible">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            {{ message }}
        </div>


.. data:: message_info
    :noindex:

    ``INFO`` alert box.

    Default:

    .. code:: html

        <div class="alert alert-info alert-dismissible">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            {{ message }}
        </div>


.. data:: message_success
    :noindex:

    ``SUCCESS`` alert box.

    Default:

    .. code:: html

        <div class="alert alert-success alert-dismissible">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            {{ message }}
        </div>


.. data:: message_warning
    :noindex:

    ``WARNING`` alert box.

    Default:

    .. code:: html

        <div class="alert alert-warning alert-dismissible">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            {{ message }}
        </div>


.. data:: message_error
    :noindex:

    ``ERROR`` alert box.

    Default:

    .. code:: html

        <div class="alert alert-error alert-dismissible">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            {{ message }}
        </div>


.. data:: message_default
    :noindex:

    Custom message alert box.

    Default:

    .. code:: html

        <div class="alert alert-info alert-dismissible">
            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
            {{ message }}
        </div>


Footer
^^^^^^

.. data:: footer_content
    :noindex:

    Footer content code.

    Default:

    .. code:: jinja

        {% block footer_content %}
            {% block footer_version %}
                <div class="pull-right hidden-xs">
                    <b>Version</b> #.#.#
                </div>
            {% endblock footer_version %}

            {% block footer_legal %}
                <strong>Copyright &copy; {% now "Y" %}.</strong> All rights reserved.
            {% endblock footer_legal %}
        {% endblock footer_content %}


.. data:: footer_version
    :noindex:

    Footer version text.

    Default:

    .. code:: jinja

        {% block footer_version %}
            <div class="pull-right hidden-xs">
                <b>Version</b> #.#.#
            </div>
        {% endblock footer_version %}


.. data:: footer_legal
    :noindex:

    Footer legal text.

    Default:

    .. code:: jinja

        {% block footer_legal %}
            <strong>Copyright &copy; {% now "Y" %}.</strong> All rights reserved.
        {% endblock footer_legal %}
