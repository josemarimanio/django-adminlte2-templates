from django.views.generic import TemplateView

from adminlte2_templates import constants as const


#
#   Default
#
class DefaultBoxedTemplateView(TemplateView):
    template_name = const.LAYOUT_DEFAULT_BOXED


class DefaultCollapsedTemplateView(TemplateView):
    template_name = const.LAYOUT_DEFAULT_COLLAPSED


class DefaultFixedTemplateView(TemplateView):
    template_name = const.LAYOUT_DEFAULT_FIXED


class DefaultLoginTemplateView(TemplateView):
    template_name = const.LAYOUT_DEFAULT_LOGIN


class DefaultRegisterTemplateView(TemplateView):
    template_name = const.LAYOUT_DEFAULT_REGISTER


class DefaultTopNavTemplateView(TemplateView):
    template_name = const.LAYOUT_DEFAULT_TOP_NAV


#
#   Barebones
#
class BarebonesBoxedTemplateView(TemplateView):
    template_name = const.LAYOUT_BAREBONES_BOXED


class BarebonesCollapsedTemplateView(TemplateView):
    template_name = const.LAYOUT_BAREBONES_COLLAPSED


class BarebonesFixedTemplateView(TemplateView):
    template_name = const.LAYOUT_BAREBONES_FIXED


class BarebonesTopNavTemplateView(TemplateView):
    template_name = const.LAYOUT_BAREBONES_TOP_NAV


#
#   No Breadcrumbs
#
class NoBreadcrumbsBoxedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_BOXED


class NoBreadcrumbsCollapsedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_COLLAPSED


class NoBreadcrumbsFixedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_FIXED


class NoBreadcrumbsTopNavTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_TOP_NAV


#
#   No Breadcrumbs, No Footer
#
class NoBreadcrumbsFooterBoxedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_FOOTER_BOXED


class NoBreadcrumbsFooterCollapsedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_FOOTER_COLLAPSED


class NoBreadcrumbsFooterFixedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_FOOTER_FIXED


class NoBreadcrumbsFooterTopNavTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_BREADCRUMBS_FOOTER_TOP_NAV


#
#   No Content Header
#
class NoContentHeaderBoxedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_CONTENT_HEADER_BOXED


class NoContentHeaderCollapsedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_CONTENT_HEADER_COLLAPSED


class NoContentHeaderFixedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_CONTENT_HEADER_FIXED


class NoContentHeaderTopNavTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_CONTENT_HEADER_TOP_NAV


#
#   No Footer
#
class NoFooterBoxedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_FOOTER_BOXED


class NoFooterCollapsedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_FOOTER_COLLAPSED


class NoFooterFixedTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_FOOTER_FIXED


class NoFooterTopNavTemplateView(TemplateView):
    template_name = const.LAYOUT_NO_FOOTER_TOP_NAV
