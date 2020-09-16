.. templates_blocks/extras


======
Extras
======


Paginator
---------

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
