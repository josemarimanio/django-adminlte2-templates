========================================
Changelog for django-adminlte2-templates
========================================


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
