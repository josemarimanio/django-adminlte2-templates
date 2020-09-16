=========
Changelog
=========


1.4.0 (Sep-17-2020)
-------------------

* Updated documentation. Added changelog page.

* Updated example project ``example_project``

* Added optional Django Admin custom AdminLTE2 theme (add ``adminlte2_admin`` to ``INSTALLED_APPS``)

* Pages
    - Login
        + Updated login form template texts from ``Login`` to ``Log In``
        + Added template block ``{% block message_template %}`` to accommodate Django ``messages``
        + Added new login form-specific template blocks ``{% block login_custom_messages %}``, ``{% block login_form_non_field_errors %}``, ``{% block login_form_fields %}``, ``{% block login_form_buttons %}``, ``{% block login_form_action %}``, ``{% block login_form_id %}``, and ``{% block login_form_method %}``
    - Register
        + Fixed HTML element ``<p class="login-box-msg">`` to ``<p class="register-box-msg">``
        + Updated register form template submit button text from ``Submit`` to ``Register``
        + Added template block ``{% block message_template %}`` to accommodate Django ``messages``
        + Added new register form-specific template blocks ``{% block register_custom_messages %}``, ``{% block register_form_non_field_errors %}``, ``{% block register_form_fields %}``, ``{% block register_form_buttons %}``, ``{% block register_form_action %}``, ``{% block register_form_id %}``, and ``{% block register_form_method %}``

* Template tags
    - Added new template tag ``{% add_attr %}`` that adds attribute name values to Django template form fields


1.3.2 (May-27-2020)
-------------------

* Fixed template tag ``{% gravatar_url %}`` to add the Gravatar ``f`` URL parameter only if ``force_default`` is ``True``

* Updated template tag ``{% add_active %}`` to support raw URL string


1.3.1 (May-16-2020)
-------------------

* Updated ``adminlte2/fix/header_dropdown_link_color.css`` to support mobile view and *top navigation* left header items

* Updated example project ``example_project``


1.3.0 (May-15-2020)
-------------------

* Updated example project ``example_project``

* Deployed a live version of the example project at https://djangoadminlte2templates.pythonanywhere.com

* Layouts
    - New component layout template ``adminlte2/components/footer_top_navigation.html`` for *top navigation* footer

* Static files
    - Updated ``jQuery`` version from ``3.4.1`` to ``3.5.1``
    - Added ``DataTables 1.10.21`` and ``Select2 4.0.13``
    - Added custom CSS ``fix/header_dropdown_link_color.css`` to fix header dropdown link colors

* Settings
    - Added new settings ``ADMINLTE_HTML_LANG_BIDI`` to manage ``<html>`` ``dir`` attribute value for handling bidirectional text
    - Added new settings ``ADMINLTE_FOOTER_VERSION`` to manage the footer version text
    - Added new settings ``ADMINLTE_STATIC_ENABLE_DATATABLES``, ``ADMINLTE_STATIC_ENABLE_FONTAWESOME``, ``ADMINLTE_STATIC_ENABLE_SELECT2`` to manage the enabling of these optional static files
    - Added new settings ``ADMINLTE_CDN_DATATABLES_CSS_CORE``, ``ADMINLTE_CDN_DATATABLES_JS_CORE`` to manage DataTables' CDN links
    - Added new settings ``ADMINLTE_CDN_SELECT2_CSS_CORE``, ``ADMINLTE_CDN_SELECT2_JS_CORE`` to manage Select2's CDN links

* Template tags
    - Fixed ‘sites’ framework support for {% page_title %} template tag
    - Updated {% gravatar_url %} template tag:
        + ``{% gravatar_url %}``  now returns a ``TemplateSyntaxError`` exception if any of the ``size``, ``default``, and ``rating`` parameters is not of valid value
        + Returned URL string is now enclosed in ``mark_safe()``, disabling string auto escape
    - Updated {% paginator %} template tag:
        + ``adjacent_pages`` parameter is now strictly applied to the left and right side of the current page link
        + ``{% paginator %}`` now returns a ``TemplateSyntaxError`` exception if the ``align`` parameter is not of valid value.
        + Added new template block ``{% paginator_id %}`` for the paginator <ul> element ``id`` attribute, defaults to ``"pagination"``
        + Paginator ``<ul>`` element is now enclosed in a ``<nav>`` tag instead of ``<div>``

* Template blocks
    - Added new block ``extra_head`` in base template for adding HTML tags in ``<head>``
    - Added new block ``html_lang_bidi`` in base template for managing ``<html>`` ``dir`` attribute
    - Added new block ``paginator_id`` in ``extras/paginator.html`` for managing the paginator element ``id`` attribute
    - Added new block ``stylesheets_fix`` in base template for custom CSS fixes

* Build
    - Added unit tests for custom template tags and filters, context processors, and template files
    - Added ESLint configuration file
    - Added StyleLint configuration file
    - Added coverage.py configuration file
    - Added tox configuration file
    - Added Codecov integration for code coverage
    - Added CodeFactor.io integration for code quality
    - Added Travis CI integration for continuous integration


1.2.0 (Apr-19-2020)
-------------------

* Updated ``{% block login_logo_href %}`` and ``{% block register_logo_href %}`` default value to ``/``
* Updated example Django project ``example_project``
* Added new ``Shortcuts`` layout template``no_breadcrumbs_footer/*`` that removes footer component and breadcrumb navigation
* Added new template tag ``{% page_title %}`` that generates text for HTML ``<title>``


1.1.0 (Apr-13-2020)
-------------------

* Fixed code to support Python 2.7 and <=Django 1.11
* Updated ``adminlte2/layouts/login.html`` to work out-of-the-box with LoginView
* Updated ``adminlte2/layouts/register.html`` to work out-of-the-box with UserCreationForm
* Updated setting ``ADMINLTE_HTML_LANG`` to base its default value from Django setting ``LANGUAGE_CODE``
* Added new template filter ``add_class`` that adds class name values to Django template form fields
* Added new template tag ``{% gravatar_url %}`` that generates a Gravatar image URL based on current user details
* Added new template tag ``{% paginator %}`` that generates an HTML code block for ``ListView`` pagination
* Added new settings ``ADMINLTE_GRAVATAR_SIZE``, ``ADMINLTE_GRAVATAR_DEFAULT``, ``ADMINLTE_GRAVATAR_FORCE_DEFAULT``, ``ADMINLTE_GRAVATAR_RATING``
