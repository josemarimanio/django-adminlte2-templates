from hashlib import md5

try:
    # Python 3
    from urllib.parse import urlencode
except ImportError:
    # Python 2.7
    from urllib import urlencode

from django import template

try:
    # Supports >=Django 2.0
    from django.shortcuts import reverse
except ImportError:
    # Supports <=Django 1.1
    from django.core.urlresolvers import reverse

from adminlte2_templates.core import get_settings

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


@register.simple_tag(takes_context=True)
def gravatar_url(context, user=None, size=None, default=None, force_default=False, rating=None):
    """
    Generate a Gravatar image URL based on the current user

    Based on:
     https://github.com/adamcharnock/django-adminlte2/tree/master/django_adminlte/templatetags.

    References:
     https://en.gravatar.com/site/implement/images/
     https://en.gravatar.com/site/implement/images/python/

    :param context: Current page context
    :type context: django.template.context.RequestContext

    :param user: User object, defaults to None (uses User object from context)
    :type user: django.contrib.auth.models.User, optional

    :param size: Image size. You may request images anywhere from 1px up to 2048px. Defaults to 80.
    :type size: int, optional

    :param default: Default image. Available options are:
        * <url>: Image URL path
        * 404: do not load any image if none is associated with the email hash, instead return an HTTP 404 response
        * mp: a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)
        * identicon: a geometric pattern based on an email hash
        * monsterid: a generated 'monster' with different colors, faces, etc
        * wavatar: generated faces with differing features and backgrounds
        * retro: awesome generated, 8-bit arcade-style pixelated faces
        * robohash: a generated robot with different colors, faces, etc
        * blank: a transparent PNG image
    :type default: str, optional

    :param force_default: Toggle to force load default image, defaults to False
    :type force_default: bool, optional

    :param rating: Image rating:
        * g: suitable for display on all websites with any audience type
        * pg: may contain rude gestures, provocatively dressed individuals, the lesser swear words, or mild violence
        * r: may contain such things as harsh profanity, intense violence, nudity, or hard drug use
        * x: may contain hardcore sexual imagery or extremely disturbing violence
    :type rating: str, optional

    :return: Gravatar image URL string
    :rtype: str
    """
    user = context['request'].user if not user else user
    params = urlencode({
        's': size or get_settings('ADMINLTE_GRAVATAR_SIZE'),
        'd': default or get_settings('ADMINLTE_GRAVATAR_DEFAULT'),
        'r': rating or get_settings('ADMINLTE_GRAVATAR_RATING'),
        'f': 'y' if get_settings('ADMINLTE_GRAVATAR_FORCE_DEFAULT') or force_default else '',
    })
    return 'https://www.gravatar.com/avatar/{hash}?{params}'.format(
        hash=md5(user.email.encode('utf-8').lower()).hexdigest() if user.is_authenticated else '',
        params=params,
    )


@register.inclusion_tag(filename='adminlte2/extras/paginator.html', takes_context=True)
def paginator(context, adjacent_pages=2, align='initial', no_margin=False):
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

        :param align: Element alignment. Valid values are ``left``, ``right``, ``center``, ``initial``.
            Defaults to ``initial``
        :type align: str, optional

        :param no_margin: Toggle to remove margin around element, defaults to ``False``.
        :type no_margin: bool, optional

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

    if align is not 'initial':
        if align == 'center':
            align = 'text-center'
        elif align == 'left':
            align = 'pull-left'
        elif align == 'right':
            align = 'pull-right'
        else:
            align = ''
    else:
        align = ''

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
        'align': align,
        'no_margin': no_margin,
    }
