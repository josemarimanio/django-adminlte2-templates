from django import template

try:
    # Supports >=Django 2.0
    from django.shortcuts import reverse
except ModuleNotFoundError:
    # Supports <=Django 1.1
    from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def add_active(context, url_pattern, *args, **kwargs):
    """
    Add class ``active`` to sidebar and header navigation links based on comparison of URL pattern with current URL.

    Based on django-adminlte2 templatetags
     https://github.com/adamcharnock/django-adminlte2/tree/master/django_adminlte/templatetags.

        :param context: Current context
        :type context: obj

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
