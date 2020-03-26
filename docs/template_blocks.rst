===============
Template Blocks
===============


Base
----

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


Page content
^^^^^^^^^^^^

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
