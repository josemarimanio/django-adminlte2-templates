Quickstart
==========

.. warning::

    This quickstart assumes you already have **django-adminlte2-templates** installed.
    If you do not, please check the `Installation <installation.html>`_ section for more details.


Using a layout template
^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    For more information on the available layout and component templates, please check the `Layouts and Components <layouts_and_components.html>`_ section.
    You may also check the `Template Blocks <template_blocks.html>`_ section for more details on the available block tags to use.

In this example, we will extend the *fixed* sidebar template (``adminlte2/layouts/fixed.html``).

Extending ``adminlte2/layouts/fixed.html``:

.. code:: jinja

    {% extends 'adminlte2/layouts/fixed.html' %}

    {% block title %}Fixed Layout{% endblock title %}

    {% block page_title %}Fixed Layout{% endblock page_title %}

    {% block page_description %}Example for extending the <i>fixed</i> sidebar template{% endblock page_description %}

    {% block breadcrumbs %}
        <li><a href="{% url 'layouts:index' %}">Layouts</a></li>
        <li><a href="{% url 'layouts:fixed' %}">Fixed</a></li>
    {% endblock breadcrumbs %}

    {% block content %}
        <div class="box">
            <div class="box-header with-border">
                <h3 class="box-title">Title</h3>
            </div>
            <div class="box-body">
                Body
            </div>
            <div class="box-footer">
                Footer
            </div>
        </div>
    {% endblock content %}


Using the extended template will generate:

.. image:: img/quickstart/using_a_layout_template_1.png


You can also override the sidebar (``adminlte2/components/sidebar.html``), header (``adminlte2/components/header.html``),
and footer (``adminlte2/components/footer.html``) component templates to update their content:


Overriding ``adminlte2/components/sidebar.html``:

.. code:: jinja

    {% extends 'adminlte2/components/sidebar.html' %}

    {% block sidebar_items %}
        <li class="treeview active">
            <a href="#">
                <i class="fa fa-circle"></i> <span>Layouts</span>
                <span class="pull-right-container">
                  <i class="fa fa-angle-left pull-right"></i>
                </span>
            </a>
            <ul class="treeview-menu">
                <li><a href="{% url 'layouts:boxed' %}"><i class="fa fa-circle-o"></i> Boxed</a></li>
                <li><a href="{% url 'layouts:collapsed' %}"><i class="fa fa-circle-o"></i> Collapsed</a></li>
                <li class="active"><a href="{% url 'layouts:fixed' %}"><i class="fa fa-circle-o"></i> Fixed</a></li>
                <li><a href="{% url 'layouts:top' %}"><i class="fa fa-circle-o"></i> Top Navigation</a></li>
            </ul>
        </li>
    {% endblock sidebar_items %}


Overriding ``adminlte2/components/header.html``:

.. code:: jinja

    {% extends 'adminlte2/components/header.html' %}

    {% block logo_lg %}
        <b>Ex</b>ample
    {% endblock logo_lg %}

    {% block logo_mini %}
        <b>Ex</b>
    {% endblock logo_mini %}

    {% block header_items %}
        <li><a href="#"><i class="fa fa-user"></i>&nbsp;&nbsp; Profile</a></li>
        <li><a href="#"><i class="fa fa-sign-out"></i>&nbsp;&nbsp; Sign Out</a></li>
    {% endblock header_items %}


Overriding ``adminlte2/components/footer.html``:

.. code:: jinja

    {% extends 'adminlte2/components/footer.html' %}

    {% block footer_version %}
        1.0.0
    {% endblock footer_version %}


Overriding the aforementioned component templates will generate:

.. image:: img/quickstart/using_a_layout_template_2.png


Setting ``settings.py`` variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    For more information on the available ``settings.py`` variables that you can use, please check the `Settings <settings.html>`_ section.


You can change the AdminLTE 2 skin theme by adding ``ADMINLTE_SKIN_THEME`` to ``settings.py``:

.. code:: python

    #
    # Valid values are: 'skin-black', 'skin-black-light', 'skin-blue', 'skin-blue-light',
    # 'skin-green', 'skin-green-light', 'skin-purple', 'skin-purple-light',
    # 'skin-red', 'skin-red-light', 'skin-yellow', 'skin-yellow-light'.
    #
    # Defaults to 'skin-blue'.
    #
    ADMINLTE_SKIN_THEME = 'skin-orange-light'


Updating the page will generate:

.. image:: img/quickstart/setting_django_settings_variables.png


Using template tags
^^^^^^^^^^^^^^^^^^^

.. note::

    For more information on the available template tags that you can use, please check the `Template Tags <template_tags.html>`_ section.


You can use the ``{% add_active %}`` template tag to automate setting the sidebar links of the current page as active.

For example, updating the sidebar ``adminlte2/components/sidebar.html`` component template:

.. code:: jinja

    {% extends 'adminlte2/components/sidebar.html' %}

    {% block sidebar_items %}
        <li class="treeview {% add_active 'layouts:index' %}">
            <a href="#">
                <i class="fa fa-circle"></i> <span>Layouts</span>
                <span class="pull-right-container">
                  <i class="fa fa-angle-left pull-right"></i>
                </span>
            </a>
            <ul class="treeview-menu">
                <li class="{% add_active 'layouts:boxed' %}"><a href="{% url 'layouts:boxed' %}"><i class="fa fa-circle-o"></i> Boxed</a></li>
                <li class="{% add_active 'layouts:collapsed' %}"><a href="{% url 'layouts:collapsed' %}"><i class="fa fa-circle-o"></i> Collapsed</a></li>
                <li class="{% add_active 'layouts:fixed' %}"><a href="{% url 'layouts:fixed' %}"><i class="fa fa-circle-o"></i> Fixed</a></li>
                <li class="{% add_active 'layouts:top' %}"><a href="{% url 'layouts:top' %}"><i class="fa fa-circle-o"></i> Top Navigation</a></li>
            </ul>
        </li>
    {% endblock sidebar_items %}
