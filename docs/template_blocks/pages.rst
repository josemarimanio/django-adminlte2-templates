.. template_blocks/pages


=====
Pages
=====


Login
-----

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

                {% block messages_template %}
                    {% include 'adminlte2/components/messages.html' %}
                {% endblock messages_template %}

                {% block login_custom_messages %}
                {% endblock login_custom_messages %}

                <p class="login-box-msg">
                    {% block login_description %}
                        Sign in to start your session
                    {% endblock login_description %}
                </p>

                {% block login_form %}
                    <form action="{% block login_form_action %}{% endblock login_form_action %}"
                          id="{% block login_form_id %}login-id{% endblock login_form_id %}"
                          method="{% block login_form_method %}POST{% endblock login_form_method %}">

                        {% csrf_token %}

                        {% if next %}
                            <input type="hidden" name="next" value="{{ next }}">
                        {% endif %}

                        {% block login_form_non_field_errors %}
                            {% if form.non_field_errors %}
                                <div class="text-danger">
                                    {{ form.non_field_errors }}
                                </div>
                            {% endif %}
                        {% endblock login_form_non_field_errors %}

                        {% block login_form_fields %}
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
                        {% endblock login_form_fields %}

                        {% block login_form_buttons %}
                            <button class="btn btn-primary" type="submit">Log in</button>
                            <button class="btn btn-default" type="reset">Clear</button>
                        {% endblock login_form_buttons %}
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


.. data:: messages_template

    Django ``messages`` alert box template.

    Default:

    .. code:: jinja

        {% block messages_template %}
            {% include 'adminlte2/components/messages.html' %}
        {% endblock messages_template %}


.. data:: login_custom_messages

    Custom Django ``messages`` alert boxes.


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
            <form action="{% block login_form_action %}{% endblock login_form_action %}"
                  id="{% block login_form_id %}login-id{% endblock login_form_id %}"
                  method="{% block login_form_method %}POST{% endblock login_form_method %}">

                {% csrf_token %}

                {% if next %}
                    <input type="hidden" name="next" value="{{ next }}">
                {% endif %}

                {% block login_form_non_field_errors %}
                    {% if form.non_field_errors %}
                        <div class="text-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}
                {% endblock login_form_non_field_errors %}

                {% block login_form_fields %}
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
                {% endblock login_form_fields %}

                {% block login_form_buttons %}
                    <button class="btn btn-primary" type="submit">Log in</button>
                    <button class="btn btn-default" type="reset">Clear</button>
                {% endblock login_form_buttons %}
            </form>
        {% endblock login_form %}


.. data:: login_form_aciton

    Login ``<form>`` tag ``action`` attribute.

    Defaults to blank.


.. data:: login_form_id

    Login ``<form>`` tag ``id`` attribute.

    Defaults to ``login-id``.


.. data:: login_form_method

    Login ``<form>`` tag ``method`` attribute.

    Defaults to ``POST``.


.. data:: login_form_non_field_errors

    Login non-field errors.

    Default:

    .. code:: jinja

        {% block login_form_non_field_errors %}
            {% if form.non_field_errors %}
                <div class="text-danger">
                    {{ form.non_field_errors }}
                </div>
            {% endif %}
        {% endblock login_form_non_field_errors %}


.. data:: login_form_fields

    Login form fields.

    Default:

    .. code:: jinja

        {% block login_form_fields %}
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
        {% endblock login_form_fields %}


.. data:: login_form_buttons

    Login form buttons.

    Default:

    .. code:: jinja

        {% block login_form_buttons %}
            <button class="btn btn-primary" type="submit">Log in</button>
            <button class="btn btn-default" type="reset">Clear</button>
        {% endblock login_form_buttons %}


.. data:: login_social_auth
    :noindex:

    Login social authentication links.


.. data:: login_links
    :noindex:

    Login links.


Register
--------

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

                <p class="register-box-msg">
                    {% block register_description %}
                        Register a new membership
                    {% endblock register_description %}
                </p>

                {% block register_form %}
                    <form action="{% block register_form_action %}{% endblock register_form_action %}"
                          id="{% block register_form_id %}register-id{% endblock register_form_id %}"
                          method="{% block register_form_method %}POST{% endblock register_form_method %}">
                        {% csrf_token %}

                        {% block register_form_non_field_errors %}
                            {% if form.non_field_errors %}
                                <div class="text-danger">
                                    {{ form.non_field_errors }}
                                </div>
                            {% endif %}
                        {% endblock register_form_non_field_errors %}

                        {% block register_form_fields %}
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
                        {% endblock register_form_fields %}

                        {% block register_form_buttons %}
                            <button class="btn btn-primary" type="submit">Submit</button>
                            <button class="btn btn-default" type="reset">Clear</button>
                        {% endblock register_form_buttons %}
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


.. data:: messages_template

    Django ``messages`` alert box template.

    Default:

    .. code:: jinja

        {% block messages_template %}
            {% include 'adminlte2/components/messages.html' %}
        {% endblock messages_template %}


.. data:: register_custom_messages

    Custom Django ``messages`` alert boxes.


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
            <form action="{% block register_form_action %}{% endblock register_form_action %}"
                  id="{% block register_form_id %}register-id{% endblock register_form_id %}"
                  method="{% block register_form_method %}POST{% endblock register_form_method %}">
                {% csrf_token %}

                {% block register_form_non_field_errors %}
                    {% if form.non_field_errors %}
                        <div class="text-danger">
                            {{ form.non_field_errors }}
                        </div>
                    {% endif %}
                {% endblock register_form_non_field_errors %}

                {% block register_form_fields %}
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
                {% endblock register_form_fields %}

                {% block register_form_buttons %}
                    <button class="btn btn-primary" type="submit">Register</button>
                    <button class="btn btn-default" type="reset">Clear</button>
                {% endblock register_form_buttons %}
            </form>
        {% endblock register_form %}


.. data:: register_form_aciton

    Register ``<form>`` tag ``action`` attribute.

    Defaults to blank.


.. data:: register_form_id

    Register ``<form>`` tag ``id`` attribute.

    Defaults to ``register-id``.


.. data:: register_form_method

    Register ``<form>`` tag ``method`` attribute.

    Defaults to ``POST``.


.. data:: register_form_non_field_errors

    Register non-field errors.

    Default:

    .. code:: jinja

        {% block register_form_non_field_errors %}
            {% if form.non_field_errors %}
                <div class="text-danger">
                    {{ form.non_field_errors }}
                </div>
            {% endif %}
        {% endblock register_form_non_field_errors %}


.. data:: register_form_fields

    Register form fields.

    Default:

    .. code:: jinja

        {% block register_form_fields %}
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
        {% endblock register_form_fields %}


.. data:: register_form_buttons

    Register form buttons.

    Default:

    .. code:: jinja

        {% block register_form_buttons %}
            <button class="btn btn-primary" type="submit">Register</button>
            <button class="btn btn-default" type="reset">Clear</button>
        {% endblock register_form_buttons %}


.. data:: register_social_auth
    :noindex:

    Register social authentication links.


.. data:: register_links
    :noindex:

    Register links.
