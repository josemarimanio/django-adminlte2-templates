===============
Template Blocks
===============


General
-------

General template tags:


<html> content
^^^^^^^^^^^^^^

.. data:: html_attribute
    :noindex:

    HTML ``<html>`` attributes.

    Default:

    .. code:: jinja

        {% block html_attribute %}lang="{% block html_lang %}{{ ADMINLTE_HTML_LANG }}{% endblock html_lang %}"{% endblock html_attribute %}


.. data:: html_lang
    :noindex:

    HTML ``<html>`` ``lang`` attribute.

    Default:

    .. code:: jinja

        {{ ADMINLTE_HTML_LANG }}


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
            {% include 'adminlte2/components/_javascripts/jquery.html' %}
            {% include 'adminlte2/components/_javascripts/bootstrap.html' %}
            {% include 'adminlte2/components/_javascripts/adminlte.html' %}
        {% endblock javascripts %}


<body> content
^^^^^^^^^^^^^^

.. data:: body
    :noindex:

    HTML ``<body>`` tag content.


.. data:: body_attribute
    :noindex:

    HTML ``<body>`` attributes.

    Default:

    .. code:: jinja

        {% block body_attribute %}class="{% block body_class %}hold-transition {{ ADMINLTE_SKIN_STYLE }}{% endblock body_class %}"{% endblock body_attribute %}


.. data:: body_class
    :noindex:

    HTML ``<body>`` tag ``class`` attributes.

    Default:

    .. code:: jinja

        {% block body_class %}hold-transition {{ ADMINLTE_SKIN_STYLE }}{% endblock body_class %}


.. data:: javascripts_body
    :noindex:

    JavaScript links in ``<body>``.


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


Pages
-----

Login
^^^^^

.. data:: login_logo
    :noindex:

    Login logo code.

    Default:

    .. code:: jinja

        {% block login_logo %}
            <div class="login-logo">
                <a href="{% block login_logo_href %}{% endblock login_logo_href %}">
                    {% block login_logo_text %}
                        <b>Admin</b>LTE
                    {% endblock login_logo_text %}
                </a>
            </div>
        {% endblock login_logo %}


.. data:: login_logo_href
    :noindex:

    Login logo link URL.


.. data:: login_logo_text
    :noindex:

    Login logo content.

    Default:

    .. code:: html

        <b>Admin</b>LTE


.. data:: login_content
    :noindex:

    Login page main content code.

    Default:

    .. code:: jinja

        {% block login_content %}
            <div class="login-box-body">

                <p class="login-box-msg">
                    {% block login_description %}
                        Sign in to start your session
                    {% endblock login_description %}
                </p>

                {% block login_form %}
                    <form method="POST">
                        {% csrf_token %}
                        {{ form }}
                    </form>
                {% endblock login_form %}

                <div class="social-auth-links text-center">
                    {% block login_social_auth %}
                    {% endblock login_social_auth %}
                </div>

                {% block login_links %}
                {% endblock login_links %}

            </div>
        {% endblock login_content %}


.. data:: login_description
    :noindex:

    Login page description.

    Default::

        Sign in to start your session


.. data:: login_form
    :noindex:

    Login form

    .. code:: jinja

        {% block login_form %}
            <form method="POST">
                {% csrf_token %}
                {{ form }}
            </form>
        {% endblock login_form %}


.. data:: login_social_auth
    :noindex:

    Login social authentication links.


.. data:: login_links
    :noindex:

    Login links.


Register
^^^^^^^^

.. data:: register_logo
    :noindex:

    Register logo code.

    Default:

    .. code:: jinja

        {% block register_logo %}
            <div class="register-logo">
                <a href="{% block register_logo_href %}{% endblock register_logo_href %}">
                    {% block register_logo_text %}
                        <b>Admin</b>LTE
                    {% endblock register_logo_text %}
                </a>
            </div>
        {% endblock register_logo %}


.. data:: register_logo_href
    :noindex:

    Register logo link URL.


.. data:: register_logo_text
    :noindex:

    Register logo content.

    Default:

    .. code:: html

        <b>Admin</b>LTE


.. data:: register_content
    :noindex:

    Register page main content code.

    Default:

    .. code:: jinja

        {% block register_content %}
            <div class="register-box-body">

                <p class="login-box-msg">
                    {% block register_description %}
                        Register a new membership
                    {% endblock register_description %}
                </p>

                {% block register_form %}
                    <form method="POST">
                        {% csrf_token %}
                        {{ form }}
                    </form>
                {% endblock register_form %}

                <div class="social-auth-links text-center">
                    {% block register_social_auth %}
                    {% endblock register_social_auth %}
                </div>

                {% block register_links %}
                {% endblock register_links %}

            </div>
        {% endblock register_content %}


.. data:: register_description
    :noindex:

    Register page description.

    Default::

        Register a new membership


.. data:: register_form
    :noindex:

    Register form

    .. code:: jinja

        {% block register_form %}
            <form method="POST">
                {% csrf_token %}
                {{ form }}
            </form>
        {% endblock register_form %}


.. data:: register_social_auth
    :noindex:

    Register social authentication links.


.. data:: register_links
    :noindex:

    Register links.
