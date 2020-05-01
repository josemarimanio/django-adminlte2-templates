from django.conf.urls import url

from tests.views.templates import *

app_name = 'templates'

urlpatterns = [
    # Default
    url(r'^default-boxed/$', DefaultBoxedTemplateView.as_view(), name='default_boxed'),
    url(r'^default-collapsed/$', DefaultCollapsedTemplateView.as_view(), name='default_collapsed'),
    url(r'^default-fixed/$', DefaultFixedTemplateView.as_view(), name='default_fixed'),
    url(r'^default-login/$', DefaultLoginTemplateView.as_view(), name='default_login'),
    url(r'^default-register/$', DefaultRegisterTemplateView.as_view(), name='default_register'),
    url(r'^default-top-nav/$', DefaultTopNavTemplateView.as_view(), name='default_top_nav'),
    # Barebones
    url(r'^barebones-boxed/$', BarebonesBoxedTemplateView.as_view(), name='barebones_boxed'),
    url(r'^barebones-collapsed/$', BarebonesCollapsedTemplateView.as_view(), name='barebones_collapsed'),
    url(r'^barebones-fixed/$', BarebonesFixedTemplateView.as_view(), name='barebones_fixed'),
    url(r'^barebones-top-nav/$', BarebonesTopNavTemplateView.as_view(), name='barebones_top_nav'),
    # No Breadcrumbs
    url(r'^no-breadcrumbs-boxed/$', NoBreadcrumbsBoxedTemplateView.as_view(), name='no_breadcrumbs_boxed'),
    url(r'^no-breadcrumbs-collapsed/$', NoBreadcrumbsCollapsedTemplateView.as_view(), name='no_breadcrumbs_collapsed'),
    url(r'^no-breadcrumbs-fixed/$', NoBreadcrumbsFixedTemplateView.as_view(), name='no_breadcrumbs_fixed'),
    url(r'^no-breadcrumbs-top-nav/$', NoBreadcrumbsTopNavTemplateView.as_view(), name='no_breadcrumbs_top_nav'),
    # No Breadcrumbs, No Footer
    url(r'^no-breadcrumbs-footer-boxed/$', NoBreadcrumbsFooterBoxedTemplateView.as_view(),
        name='no_breadcrumbs_footer_boxed'),
    url(r'^no-breadcrumbs-footer-collapsed/$', NoBreadcrumbsFooterCollapsedTemplateView.as_view(),
        name='no_breadcrumbs_footer_collapsed'),
    url(r'^no-breadcrumbs-footer-fixed/$', NoBreadcrumbsFooterFixedTemplateView.as_view(),
        name='no_breadcrumbs_footer_fixed'),
    url(r'^no-breadcrumbs-footer-top-nav/$', NoBreadcrumbsFooterTopNavTemplateView.as_view(),
        name='no_breadcrumbs_footer_top_nav'),
    # No Content Header
    url(r'^no-content-header-boxed/$', NoContentHeaderBoxedTemplateView.as_view(),
        name='no_content_header_boxed'),
    url(r'^no-content-header-collapsed/$', NoContentHeaderCollapsedTemplateView.as_view(),
        name='no_content_header_collapsed'),
    url(r'^no-content-header-fixed/$', NoContentHeaderFixedTemplateView.as_view(),
        name='no_content_header_fixed'),
    url(r'^no-content-header-top-nav/$', NoContentHeaderTopNavTemplateView.as_view(),
        name='no_content_header_top_nav'),
    # No Footer
    url(r'^no-footer-boxed/$', NoFooterBoxedTemplateView.as_view(), name='no_footer_boxed'),
    url(r'^no-footer-collapsed/$', NoFooterCollapsedTemplateView.as_view(), name='no_footer_collapsed'),
    url(r'^no-footer-fixed/$', NoFooterFixedTemplateView.as_view(), name='no_footer_fixed'),
    url(r'^no-footer-top-nav/$', NoFooterTopNavTemplateView.as_view(), name='no_footer_top_nav'),
]
