======================
Layouts and Components
======================


Layouts
-------

.. data:: adminlte2/base.html
    :noindex:

    Base AdminLTE 2 layout template.


.. data:: adminlte2/layouts/boxed.html
    :noindex:

    AdminLTE 2 template for *boxed* layout option.

    See `https://adminlte.io/themes/AdminLTE/pages/layout/boxed.html <https://adminlte.io/themes/AdminLTE/pages/layout/boxed.html>`_ for a live example of this template.


.. data:: adminlte2/layouts/collapsed_sidebar.html
    :noindex:

    AdminLTE 2 template for *collapsed sidebar* layout option.

    See `https://adminlte.io/themes/AdminLTE/pages/layout/collapsed-sidebar.html <https://adminlte.io/themes/AdminLTE/pages/layout/collapsed-sidebar.html>`_ for a live example of this template.


.. data:: adminlte2/layouts/fixed.html
    :noindex:

    AdminLTE 2 template for *fixed* layout option.

    See `https://adminlte.io/themes/AdminLTE/pages/layout/fixed.html <https://adminlte.io/themes/AdminLTE/pages/layout/fixed.html>`_ for a live example of this template.


.. data:: adminlte2/layouts/top_navigation.html
    :noindex:

    AdminLTE 2 template for *top navigation* layout option.

    See `https://adminlte.io/themes/AdminLTE/pages/layout/top-nav.html <https://adminlte.io/themes/AdminLTE/pages/layout/top-nav.html>`_ for a live example of this template.


.. data:: adminlte2/layouts/login.html
    :noindex:

    AdminLTE 2 login page template.

    See `https://adminlte.io/themes/AdminLTE/pages/examples/login.html <https://adminlte.io/themes/AdminLTE/pages/examples/login.html>`_ for a live example of this template.


.. data:: adminlte2/layouts/register.html
    :noindex:

    AdminLTE 2 register page template.

    See `https://adminlte.io/themes/AdminLTE/pages/examples/register.html <https://adminlte.io/themes/AdminLTE/pages/examples/register.html>`_ for a live example of this template.


Components
----------

.. data:: adminlte2/components/sidebar.html
    :noindex:

    Sidebar navigation template.

    Please check the `Template Blocks <template_blocks.html>`_  > `Layouts <template_blocks.html#layouts>`_ > `Sidebar <template_blocks.html#sidebar>`_ section
    for more information on the available template blocks that can be used to customize this component.


.. data:: adminlte2/components/control.html
    :noindex:

    Control navigation template.

    Please check the `Template Blocks <template_blocks.html>`_ > `Layouts <template_blocks.html#layouts>`_ > `Control <template_blocks.html#control>`_ section
    for more information on the available template blocks that can be used to customize this component.


.. data:: adminlte2/components/header.html
    :noindex:

    Header navigation bar template for *boxed*, *collapsed sidebar*, and *fixed* layout options.

    Please check the `Template Blocks <template_blocks.html>`_ > `Layouts <template_blocks.html#layouts>`_ > `Header <template_blocks.html#header>`_ section
    for more information on the available template blocks that can be used to customize this component.


.. data:: adminlte2/components/header_top_navigation.html
    :noindex:

    Header navigation bar template for *top navigation* layout option.

    Please check the `Template Blocks <template_blocks.html>`_ > `Layouts <template_blocks.html#layouts>`_ > `Header <template_blocks.html#header>`_ section
    for more information on the available template blocks that can be used to customize this component.


.. data:: adminlte2/components/messages.html
    :noindex:

    *Django Messages* alert box template.

    Please check the `Template Blocks <template_blocks.html>`_ > `Layouts <template_blocks.html#layouts>`_ > `Messages <template_blocks.html#header>`_ section
    for more information on the available template blocks that can be used to customize this component.


.. data:: adminlte2/components/footer.html
    :noindex:

    Footer template.

    Please check the `Template Blocks <template_blocks.html>`_ > `Layouts <template_blocks.html#layouts>`_ > `Footer <template_blocks.html#footer>`_ section
    for more information on the available template blocks that can be used to customize this component.


Shortcuts
---------

**django-adminlte2-templates** provides shortcuts to some commonly-used layout template modifications:


.. data:: adminlte2/shortcuts/barebones/*
    :noindex:

    Remove content header (page title, page description, breadcrumb navigation), footer, and control sidebar for
    ``boxed.html``, ``collapsed_sidebar.html``, ``fixed.html``, and ``top_navigation.html``.


.. data:: adminlte2/shortcuts/no_content_header/*
    :noindex:

    Remove content header (page title, page description, breadcrumb navigation) for
    ``boxed.html``, ``collapsed_sidebar.html``, ``fixed.html``, and ``top_navigation.html``.


.. data:: adminlte2/shortcuts/no_breadcrumbs/*
    :noindex:

    Remove breadcrumb navigation for
    ``boxed.html``, ``collapsed_sidebar.html``, ``fixed.html``, and ``top_navigation.html``.


.. data:: adminlte2/shortcuts/no_footer/*
    :noindex:

    Remove footer for
    ``boxed.html``, ``collapsed_sidebar.html``, ``fixed.html``, and ``top_navigation.html``.


.. data:: adminlte2/shortcuts/no_breadcrumbs_footer/*
    :noindex:

    Remove footer and breadcrumb navigation for
    ``boxed.html``, ``collapsed_sidebar.html``, ``fixed.html``, and ``top_navigation.html``.


Extras
------

.. data:: adminlte2/extras/paginator.html
    :noindex:

    Layout template file for template tag ``{% paginator %}``.
    Please check the `Template Tags <template_tags.html>`_ > `Tags <template_tags.html#tags>`_ section for more information on ``{% paginator %}``.
