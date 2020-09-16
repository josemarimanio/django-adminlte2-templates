.. template_blocks/layouts


=======
Layouts
=======

*Sidebar* and *top navigation* layout template blocks:


Templates
---------

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
-------

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
------

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
-------

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
-------

Template blocks to customize the control component (``adminlte2/components/control.html``):


.. data:: control_items
    :noindex:

    Control sidebar navigation items.


.. data:: control_tabs
    :noindex:

    Control sidebar navigation tab contents.


Messages
--------

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
------

Template blocks to customize the footer components (``adminlte2/components/footer.html``), (``adminlte2/components/footer_top_navigation``):

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
