===============
Template Blocks
===============


General
-------


<html> content
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^

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


Layouts
-------

*Sidebar* and *top navigation* layout template blocks:


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

        {% block control_template %}
            {% include 'adminlte2/components/control.html %}
        {% endblock control_template %}


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
                {% block content_wrapper %}
                    {% block no_content_header %}
                        <section class="content-header">
                            {% block content_header %}
                                {% block no_page_title %}
                                    <h1>
                                        {% block page_title %}{% endblock page_title %}
                                        <small>{% block page_description %}{% endblock page_description %}</small>
                                    </h1>
                                {% endblock no_page_title %}

                                {% block no_breadcrumbs %}
                                    <ol class="breadcrumb">
                                        {% block breadcrumbs %}{% endblock breadcrumbs %}
                                    </ol>
                                {% endblock no_breadcrumbs %}
                            {% endblock content_header %}
                        </section>
                    {% endblock no_content_header %}

                    {% block content_body %}
                        <section class="content">
                            {% block messages_template %}
                                {% include 'adminlte2/components/messages.html' %}
                            {% endblock messages_template %}

                            {% block content %}
                            {% endblock content %}
                        </section>
                    {% endblock content_body %}
                {% endblock content_wrapper %}
            </div>
        {% endblock content_template %}


.. data:: content_wrapper
    :noindex:

    Page content ``<div class="content-wrapper">`` code.


.. data:: content_header
    :noindex:

    Page content header code. Contains the page title and description, and breadcrumb navigation.

    Default:

    .. code:: jinja

        {% block content_header %}
            {% block no_page_title %}
                <h1>
                    {% block page_title %}{% endblock page_title %}
                    <small>{% block page_description %}{% endblock page_description %}</small>
                </h1>
            {% endblock no_page_title %}

            {% block no_breadcrumbs %}
                <ol class="breadcrumb">
                    {% block breadcrumbs %}{% endblock breadcrumbs %}
                </ol>
            {% endblock no_breadcrumbs %}
        {% endblock content_header %}


.. data:: no_content_header
    :noindex:

    Declare block as empty to remove page content header (page title and description, breadcrumb navigation):

    .. code:: jinja

        {% block no_content_header %}{% endblock no_content_header %}


.. data:: page_title
    :noindex:

    Page title text that will be displayed in the content header.


.. data:: page_description
    :noindex:

    Page description text that will be displayed in the content header.


.. data:: no_page_title
    :noindex:

    Declare block as empty to remove page title and description text:

    .. code:: jinja

        {% block no_page_title %}{% endblock no_page_title %}


.. data:: breadcrumbs
    :noindex:

    Breadcrumb navigation that will be displayed in the content header.


.. data:: no_breadcrumbs
    :noindex:

    Declare block as empty to remove breadcrumb navigation:

    .. code:: jinja

        {% block no_breadcrumbs %}{% endblock no_breadcrumbs %}


.. data:: content_body
    :noindex:

    Page content body code. Contains the Django ``messages`` alert boxes and page main content.

    Default:

    .. code:: jinja

        {% block content_body %}
            <section class="content">
                {% block messages_template %}
                    {% include 'adminlte2/components/messages.html' %}
                {% endblock messages_template %}

                {% block content %}
                {% endblock content %}
            </section>
        {% endblock content_body %}


.. data:: content
    :noindex:

    Page main content.


Header
^^^^^^

Template blocks to customize the header component (``adminlte2/components/header.html``, ``adminlte2/components/header_top_navigation.html``).

**django-adminlte2-templates** supports header for both  **sidebar** (*boxed, collapsed, fixed*) and
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

    Defaults to ``/``.


.. data:: logo_mini
    :noindex:

    (*sidebar* only) Header logo content when the *sidebar* content is collapsed.

    Default:

    .. code:: jinja

        {% block logo_mini %}<b>A</b>LTE{% endblock logo_mini %}


.. data:: logo_lg
    :noindex:

    Header logo content when *sidebar* content is exposed, or for *top navigation* layout.

    Default:

    .. code:: jinja

        {% block logo_lg %}<b>Admin</b>LTE{% endblock logo_lg %}


.. data:: header_content
    :noindex:

    Header main content code.

    Default for *sidebar*:

    .. code:: jinja

        {% block header_content %}
            <nav class="navbar navbar-static-top">
                {% block sidebar_toggle %}
                    <a href="#" class="sidebar-toggle" data-toggle="push-menu" role="button">
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
            <a href="#" class="sidebar-toggle" data-toggle="push-menu" role="button">
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

    Defaults to ``Toggle navigation``.


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

    Defaults to ``Toggle navigation``.


Sidebar
^^^^^^^

Template blocks to customize the sidebar component (``adminlte2/components/sidebar.html``):


.. data:: sidebar_title
    :noindex:

    Sidebar navigation title text.

    Default:

    .. code:: jinja

        <li class="header">{% block sidebar_title %}MAIN NAVIGATION{% endblock sidebar_title %}</li>


.. data:: no_sidebar_title
    :noindex:

    Declare block as empty to remove sidebar title:

    .. code:: jinja

        {% block no_sidebar_title %}{% endblock no_sidebar_title %}


.. data:: sidebar_form
    :noindex:

    Sidebar space for form elements.


.. data:: sidebar_items
    :noindex:

    Sidebar navigation items.


Control
^^^^^^^

Template blocks to customize the control component (``adminlte2/components/control.html``):


.. data:: control_items
    :noindex:

    Control sidebar navigation items.


.. data:: control_tabs
    :noindex:

    Control sidebar navigation tab contents.


Messages
^^^^^^^^

Template blocks to customize the Django ``messages`` alert boxes component (``adminlte2/components/messages.html``):


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

Template blocks to customize the footer component (``adminlte2/components/footer.html``):


.. data:: footer_content
    :noindex:

    Footer content code.

    Default:

    .. code:: jinja

        {% block footer_content %}

            <div class="pull-right hidden-xs">
                {% block footer_right %}
                    <b>Version</b> {% block footer_version %}#.#.#{% endblock footer_version %}
                {% endblock footer_right %}
            </div>

            {% block footer_left %}
                {% block footer_legal %}
                    <strong>Copyright &copy; {% now "Y" %}.</strong> All rights reserved.
                {% endblock footer_legal %}
            {% endblock footer_left %}

        {% endblock footer_content %}


.. data:: footer_left
    :noindex:

    Footer left side content.

    Default:

    .. code:: jinja

        {% block footer_left %}
            {% block footer_legal %}
                <strong>Copyright &copy; {% now "Y" %}.</strong> All rights reserved.
            {% endblock footer_legal %}
        {% endblock footer_left %}


.. data:: footer_right
    :noindex:

    Footer right side content.

    Default:

    .. code:: jinja

        <div class="pull-right hidden-xs">
            {% block footer_right %}
                <b>Version</b> {% block footer_version %}{{ ADMINLTE_FOOTER_VERSION }}{% endblock footer_version %}
            {% endblock footer_right %}
        </div>


.. data:: footer_version
    :noindex:

    Footer version text.

    Default:

    .. code:: jinja

        <b>Version</b> {% block footer_version %}{{ ADMINLTE_FOOTER_VERSION }}{% endblock footer_version %}


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
                <a href="{% block login_logo_href %}/{% endblock login_logo_href %}">
                    {% block login_logo_text %}
                        <b>Admin</b>LTE
                    {% endblock login_logo_text %}
                </a>
            </div>
        {% endblock login_logo %}


.. data:: login_logo_href
    :noindex:

    Login logo link URL.

    Defaults to ``/``.


.. data:: login_logo_text
    :noindex:

    Login logo content.

    Default:

    .. code:: html

        {% block login_logo_text %}
            <b>Admin</b>LTE
        {% endblock login_logo_text %}


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
                        {% if next %}
                            <input type="hidden" name="next" value="{{ next }}">
                        {% endif %}
                        {% if form.non_field_errors %}
                            <div class="text-danger">
                                {{ form.non_field_errors }}
                            </div>
                        {% endif %}
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
                        <button class="btn btn-primary" type="submit">Submit</button>
                        <button class="btn btn-default" type="reset">Clear</button>
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

    Defaults to ``Sign in to start your session``.


.. data:: login_form
    :noindex:

    Login form code.

    Default:

    .. code:: jinja

        {% block login_form %}
            <form method="POST">
                {% csrf_token %}
                {% if next %}
                    <input type="hidden" name="next" value="{{ next }}">
                {% endif %}
                {% if form.non_field_errors %}
                    <div class="text-danger">
                        {{ form.non_field_errors }}
                    </div>
                {% endif %}
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
                <button class="btn btn-primary" type="submit">Submit</button>
                <button class="btn btn-default" type="reset">Clear</button>
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
                <a href="{% block register_logo_href %}/{% endblock register_logo_href %}">
                    {% block register_logo_text %}
                        <b>Admin</b>LTE
                    {% endblock register_logo_text %}
                </a>
            </div>
        {% endblock register_logo %}


.. data:: register_logo_href
    :noindex:

    Register logo link URL.

    Defaults to ``/``.


.. data:: register_logo_text
    :noindex:

    Register logo content.

    Default:

    .. code:: html

        {% block register_logo_text %}
            <b>Admin</b>LTE
        {% endblock register_logo_text %}


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
                        {% if form.non_field_errors %}
                            <div class="text-danger">
                                {{ form.non_field_errors }}
                            </div>
                        {% endif %}
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
                        <button class="btn btn-primary" type="submit">Submit</button>
                        <button class="btn btn-default" type="reset">Clear</button>
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

    Defaults to ``Register a new membership``.


.. data:: register_form
    :noindex:

    Register form code.

    Default:

    .. code:: jinja

        {% block register_form %}
            <form method="POST">
                {% csrf_token %}
                {% if form.non_field_errors %}
                    <div class="text-danger">
                        {{ form.non_field_errors }}
                    </div>
                {% endif %}
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
                <button class="btn btn-primary" type="submit">Submit</button>
                <button class="btn btn-default" type="reset">Clear</button>
            </form>
        {% endblock register_form %}


.. data:: register_social_auth
    :noindex:

    Register social authentication links.


.. data:: register_links
    :noindex:

    Register links.


Extras
------


Paginator
^^^^^^^^^

.. data:: paginator_template
    :noindex:

    Paginator template

    Default:

    .. code:: jinja

        {% block paginator_template %}

        <nav {% if align %}class="{{ align }}"{% endif %}>
            <ul id="{% block paginator_id %}pagination{% endblock paginator_id %}" class="{% block paginator_class %}pagination{% if no_margin %} no-margin{% endif %}{% endblock paginator_class %}">
                {% block paginator_content %}
                    {% block first %}
                        {% if show_first %}
                            <li>
                                <a href="?page=1">
                                    {% block first_text %}<small>First</small>{% endblock first_text %}
                                </a>
                            </li>
                        {% endif %}
                    {% endblock first %}

                    {% block prev %}
                        {% if has_prev %}
                            <li>
                                <a href="?page={{ prev_page }}">
                                    {% block prev_text %}<i class="fa fa-caret-left"></i>{% endblock prev_text %}
                                </a>
                            </li>
                        {% endif %}
                    {% endblock prev %}

                    {% block pages %}
                        {% for link_page in page_numbers %}
                            {% ifequal link_page current_page %}
                                {% block current %}
                                    <li class="active">
                                        <a href="?page={{ link_page }}">
                                            {% block current_text %}
                                                {{ current_page }}
                                            {% endblock current_text %}
                                        </a>
                                    </li>
                                {% endblock current %}
                            {% else %}
                                {% block link %}
                                    <li>
                                        <a href="?page={{ link_page }}">
                                            {% block link_text %}
                                                {{ link_page }}
                                            {% endblock link_text %}
                                        </a>
                                    </li>
                                {% endblock link %}
                            {% endifequal %}
                        {% endfor %}
                    {% endblock pages %}

                    {% block next %}
                        {% if has_next %}
                            <li>
                                <a href="?page={{ next_page }}">
                                    {% block next_text %}
                                        <i class="fa fa-caret-right"></i>
                                    {% endblock next_text %}
                                </a>
                            </li>
                        {% endif %}
                    {% endblock next %}

                    {% block last %}
                        {% if show_last %}
                            <li>
                                <a href="?page=last">
                                    {% block last_text %}<small>Last</small>{% endblock last_text %}
                                </a>
                            </li>
                        {% endif %}
                    {% endblock last %}
                {% endblock paginator_content %}
            </ul>
        </nav>

        {% endblock paginator_template %}


.. data:: paginator_id
    :noindex:

    Paginator element ``id`` attribute, defaults to ``pagination``.


.. data:: paginator_class
    :noindex:

    Paginator element class names.

    Default:

    .. code:: jinja

        class="{% block paginator_class %}pagination{% if no_margin %} no-margin{% endif %}{% endblock paginator_class %}"


.. data:: paginator_content
    :noindex:

    Paginator main content code.


.. data:: first
    :noindex:

    First page link code.

    Default:

    .. code:: jinja

        {% block first %}
            {% if show_first %}
                <li>
                    <a href="?page=1">
                        {% block first_text %}<small>First</small>{% endblock first_text %}
                    </a>
                </li>
            {% endif %}
        {% endblock first %}


.. data:: first_text
    :noindex:

    First page link text.

    Default:

    .. code:: jinja

        {% block first_text %}<small>First</small>{% endblock first_text %}


.. data:: prev
    :noindex:

    Previous page link code.

    Default:

    .. code:: jinja

        {% block prev %}
            {% if has_prev %}
                <li>
                    <a href="?page={{ prev_page }}">
                        {% block prev_text %}<i class="fa fa-caret-left"></i>{% endblock prev_text %}
                    </a>
                </li>
            {% endif %}
        {% endblock prev %}


.. data:: prev_text
    :noindex:

    Previous page link text.

    Default:

    .. code:: jinja

        {% block prev_text %}<i class="fa fa-caret-left"></i>{% endblock prev_text %}


.. data:: pages
    :noindex:

    Page number links code.

    Default:

    .. code:: jinja

        {% block pages %}
            {% for link_page in page_numbers %}
                {% ifequal link_page current_page %}
                    {% block current %}
                        <li class="active">
                            <a href="?page={{ link_page }}">
                                {% block current_text %}
                                    {{ current_page }}
                                {% endblock current_text %}
                            </a>
                        </li>
                    {% endblock current %}
                {% else %}
                    {% block link %}
                        <li>
                            <a href="?page={{ link_page }}">
                                {% block link_text %}
                                    {{ link_page }}
                                {% endblock link_text %}
                            </a>
                        </li>
                    {% endblock link %}
                {% endifequal %}
            {% endfor %}
        {% endblock pages %}


.. data:: current
    :noindex:

    Current page number link code.

    Default:

    .. code:: jinja

        {% block current %}
            <li class="active">
                <a href="?page={{ link_page }}">
                    {% block current_text %}
                        {{ current_page }}
                    {% endblock current_text %}
                </a>
            </li>
        {% endblock current %}


.. data:: current_text
    :noindex:

    Current page number link text.

    Default:

    .. code:: jinja

        {% block current_text %}
            {{ current_page }}
        {% endblock current_text %}


.. data:: link
    :noindex:

    Adjacent page number link code.

    Default:

    .. code:: jinja

        {% block link %}
            <li>
                <a href="?page={{ link_page }}">
                    {% block link_text %}
                        {{ link_page }}
                    {% endblock link_text %}
                </a>
            </li>
        {% endblock link %}


.. data:: link_text

    Adjacent page number link text.

    Default:

    .. code:: jinja

        {% block link_text %}
            {{ link_page }}
        {% endblock link_text %}


.. data:: next

    Next page link code.

    Default

    .. code:: jinja

        {% block next %}
            {% if has_next %}
                <li>
                    <a href="?page={{ next_page }}">
                        {% block next_text %}
                            <i class="fa fa-caret-right"></i>
                        {% endblock next_text %}
                    </a>
                </li>
            {% endif %}
        {% endblock next %}


.. data:: next_text

    Next page link text.

    Default:

    .. code:: jinja

        {% block next_text %}
            <i class="fa fa-caret-right"></i>
        {% endblock next_text %}


.. data:: last

    Last page link code.

    Default:

    .. code:: jinja

        {% block last %}
            {% if show_last %}
                <li>
                    <a href="?page=last">
                        {% block last_text %}<small>Last</small>{% endblock last_text %}
                    </a>
                </li>
            {% endif %}
        {% endblock last %}


.. data:: last_text

    Last page link text.

    Default:

    .. code:: jinja

        {% block last_text %}<small>Last</small>{% endblock last_text %}
