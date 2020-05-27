import hashlib

from django import template
from django.core.exceptions import ImproperlyConfigured
from django.urls.exceptions import NoReverseMatch
from django.utils.safestring import mark_safe
from django.template.exceptions import TemplateSyntaxError

from adminlte2_templates import constants as const
from adminlte2_templates.core import get_settings
from adminlte2_templates.core import reverse
from adminlte2_templates.core import urlencode

try:
    # {% page_title %} Django 'sites' framework support
    from django.contrib.sites.models import Site
    from django.contrib.sites.shortcuts import get_current_site
except RuntimeError:
    pass

register = template.Library()


@register.simple_tag(takes_context=True)
def add_active(context, url_pattern, *args, **kwargs):
    """
    Add class ``active`` to sidebar and header navigation links based on comparison of URL pattern with current URL.

    Based on django-adminlte2 templatetags
     https://github.com/adamcharnock/django-adminlte2/tree/master/django_adminlte/templatetags.

        :param context: Current page context
        :type context: django.template.context.RequestContext

        :param url_pattern: URL pattern for ``reverse`` matching or raw URL string
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

    try:
        path = reverse(url_pattern, args=args, kwargs=kwargs)
    except NoReverseMatch:
        path = url_pattern

    current_path = context.request.path

    if not_when and any(nw in current_path for nw in not_when):
        return ''
    elif not exact_match and current_path.startswith(path) or exact_match and current_path == path:
        return ' active '
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
def gravatar_url(context, user=None, size=None, default=None, force_default=None, rating=None):
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
    size = size or get_settings('ADMINLTE_GRAVATAR_SIZE')
    default = default or get_settings('ADMINLTE_GRAVATAR_DEFAULT')
    rating = rating or get_settings('ADMINLTE_GRAVATAR_RATING')
    user = context['request'].user if not user else user

    if not const.GRAVATAR_SIZE_MINIMUM <= size <= const.GRAVATAR_SIZE_MAXIMUM:
        raise TemplateSyntaxError('"size" parameter only allows int values from {} to {}'.format(
            const.GRAVATAR_SIZE_MINIMUM, const.GRAVATAR_SIZE_MAXIMUM
        ))

    if default not in const.GRAVATAR_DEFAULT_CHOICES:
        raise TemplateSyntaxError(
            '"default" parameter valid values are: {}'.format(', '.join(const.GRAVATAR_DEFAULT_CHOICES)))

    if rating not in const.GRAVATAR_RATING_CHOICES:
        raise TemplateSyntaxError(
            '"rating" parameter valid values are: {}'.format(', '.join(const.GRAVATAR_RATING_CHOICES)))

    if force_default is None:
        force_default = get_settings('ADMINLTE_GRAVATAR_FORCE_DEFAULT')

    params = [
        ('s', size),
        ('d', default),
        ('r', rating),
    ]

    if force_default:
        params.append(('f', 'y'))

    params = urlencode(params)

    return mark_safe('https://www.gravatar.com/avatar/{hash}?{params}'.format(  # nosec
        hash=hashlib.md5(user.email.encode('utf-8').lower()).hexdigest() if user.is_authenticated else '',  # nosec
        params=params,
    ))


@register.inclusion_tag(filename=const.PAGINATOR_TEMPLATE_NAME, takes_context=True)
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

    if align == const.PAGINATOR_ALIGN_INITIAL:
        align = ''
    elif align == const.PAGINATOR_ALIGN_CENTER:
        align = 'text-center'
    elif align == const.PAGINATOR_ALIGN_LEFT:
        align = 'pull-left'
    elif align == const.PAGINATOR_ALIGN_RIGHT:
        align = 'pull-right'
    else:
        raise TemplateSyntaxError(
            '"align" parameter valid values are: {}'.format(', '.join(const.PAGINATOR_ALIGN_CHOICES)))

    start_page = max(current_page - adjacent_pages, 1)

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


@register.simple_tag(takes_context=True)
def page_title(context, page_name=''):
    """
    Generate text for HTML <title>. Supports Django 'sites' framework and 'ListView' pagination.

    :param context: Current page context
    :type context: django.template.context.RequestContext

    :param page_name: Page title text. Adding 'page_name' to the page context will override this parameter.
        Defaults to ''.
    :type page_name: str, optional

    :return: Title text
    :rtype: str
    """

    # Check if pagination is enabled
    page_obj = context.get('page_obj', None)
    paginator = context.get('paginator', None)

    title_format = get_settings('ADMINLTE_TITLE_FORMAT')
    title_pagination_format = get_settings('ADMINLTE_TITLE_FORMAT_PAGINATION')
    divider = get_settings('ADMINLTE_TITLE_DIVIDER')
    site_name = get_settings('ADMINLTE_TITLE_SITE')

    try:
        # Check current page context to override 'page_name' parameter
        page_name = context['page_name']
    except KeyError:
        pass

    try:
        # Get current Site object by SITE_ID
        site_name = Site.objects.get_current().name
    except NameError:
        # If 'sites' is not in INSTALLED_APPS, get site title from settings.py
        pass
    except (ImproperlyConfigured, Site.DoesNotExist):
        # Else if an invalid SITE_ID is provided, get value from current page context
        try:
            site_name = get_current_site(context['request']).name
        except Site.DoesNotExist:
            pass

    params = {
        'site': site_name,
        'divider': divider,
        'page': page_name,
    }

    if page_obj and paginator:
        # If {% page_title %} is used in a ListView, use the title format string with pagination support
        title_format = title_pagination_format
        params.update({'curr_no': page_obj.number, 'last_no': paginator.num_pages, })

    return title_format.format(**params)
