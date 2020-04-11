from django import template

try:
    # Supports >=Django 2.0
    from django.shortcuts import reverse
except ImportError:
    # Supports <=Django 1.1
    from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def add_active(context, url_pattern, *args, **kwargs):
    """
    Add class ``active`` to sidebar and header navigation links based on comparison of URL pattern with current URL.

    Based on django-adminlte2 templatetags
     https://github.com/adamcharnock/django-adminlte2/tree/master/django_adminlte/templatetags.

        :param context: Current page context
        :type context: django.template.context.RequestContext

        :param url_pattern: URL pattern for ``reverse`` matching
        :type url_pattern: str

        :param exact_match: Toggle for exact matching, defaults to False
        :type exact_match: bool, optional

        :param not_when: Comma-separated values of string patterns
            that will render comparison as False, defaults to ''
        :type not_when: str, optional

        :param args: Positional arguments for ``reverse`` matching
        :type args: tuple

        :params kwargs: Keyword arguments for ``reverse`` matching
        :type kwargs: dict

        :return: 'active' if comparison is True, else ''
        :rtype: str
    """
    exact_match = kwargs.pop('exact_match', False)
    not_when = kwargs.pop('not_when', '').split(',')
    not_when = [nw.strip() for nw in not_when if nw.strip()]

    path = reverse(url_pattern, args=args, kwargs=kwargs)
    current_path = context.request.path

    if not_when and any(nw in current_path for nw in not_when):
        return ''

    if not exact_match and current_path.startswith(path):
        return ' active '
    elif exact_match and current_path == path:
        return ' active '
    else:
        return ''


@register.filter
def add_class(field, class_name):
    """
    Add class names to a form field

    Based on a StackOverflow answer:
     https://stackoverflow.com/a/27284041

        :param field: Django Form element
        :type field: django.forms.boundfield.BoundField

        :param class_name: HTML class name value
        :type class_name: django.utils.safestring.SafeString

        :return: Rendered Django Form element with newly-added class name values
        :rtype: django.utils.safestring.SafeString
    """
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })


@register.inclusion_tag(filename='adminlte2/extras/paginator.html', takes_context=True)
def paginator(context, adjacent_pages=2):
    """
    Adds pagination context variables for use in displaying first, adjacent and last page links in addition
    to those created by the object_list generic view.

    Based on:
     http://www.djangosnippets.org/snippets/73/
     http://www.tummy.com/Community/Articles/django-pagination/

        :param context: Current page context
        :type context: django.template.context.RequestContext

        :param adjacent_pages: Adjacent page links to current page link, defaults to 2
        :type adjacent_pages: int, optional

        :return: Paginator page context:

            * page_obj     - paginated list objects
            * paginator    - paginator object
            * current_page - current page number
            * last_page    - last page number
            * page_numbers - total number of pages
            * has_prev     - toggle to show previous page link
            * has_next     - toggle to show next page link
            * prev_page    - previous page number
            * next_page    - next page number
            * show_first   - toggle to show first page link
            * show_last    - toggle to show last page link
        :rtype: dict
    """
    page_obj = context['page_obj']
    paginator = context['paginator']
    current_page = page_obj.number
    number_of_pages = paginator.num_pages

    start_page = max(current_page - adjacent_pages, 1)
    if start_page <= 3:
        start_page = 1

    end_page = current_page + adjacent_pages + 1
    if end_page > number_of_pages:
        end_page = number_of_pages + 1

    page_numbers = [n for n in range(start_page, end_page) if 0 < n <= number_of_pages]

    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'current_page': current_page,
        'last_page': number_of_pages,
        'page_numbers': page_numbers,
        'has_prev': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'prev_page': page_obj.previous_page_number,
        'next_page': page_obj.next_page_number,
        'show_first': 1 != current_page,
        'show_last': number_of_pages != current_page,
    }
