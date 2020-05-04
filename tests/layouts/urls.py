from django.conf.urls import url

from . import views

app_name = 'layouts'

urlpatterns = [
    #
    #   Default
    #
    url(r'^default-boxed/$',
        views.DefaultBoxedTemplateView.as_view(), name='default_boxed'),
    url(r'^default-collapsed/$',
        views.DefaultCollapsedTemplateView.as_view(), name='default_collapsed'),
    url(r'^default-fixed/$',
        views.DefaultFixedTemplateView.as_view(), name='default_fixed'),
    url(r'^default-login/$',
        views.DefaultLoginTemplateView.as_view(), name='default_login'),
    url(r'^default-register/$',
        views.DefaultRegisterTemplateView.as_view(), name='default_register'),
    url(r'^default-top-nav/$',
        views.DefaultTopNavTemplateView.as_view(), name='default_top_nav'),
    #
    #   Barebones
    #
    url(r'^barebones-boxed/$',
        views.BarebonesBoxedTemplateView.as_view(), name='barebones_boxed'),
    url(r'^barebones-collapsed/$',
        views.BarebonesCollapsedTemplateView.as_view(), name='barebones_collapsed'),
    url(r'^barebones-fixed/$',
        views.BarebonesFixedTemplateView.as_view(), name='barebones_fixed'),
    url(r'^barebones-top-nav/$',
        views.BarebonesTopNavTemplateView.as_view(), name='barebones_top_nav'),
    #
    #   No Breadcrumbs
    #
    url(r'^no-breadcrumbs-boxed/$',
        views.NoBreadcrumbsBoxedTemplateView.as_view(), name='no_breadcrumbs_boxed'),
    url(r'^no-breadcrumbs-collapsed/$',
        views.NoBreadcrumbsCollapsedTemplateView.as_view(), name='no_breadcrumbs_collapsed'),
    url(r'^no-breadcrumbs-fixed/$',
        views.NoBreadcrumbsFixedTemplateView.as_view(), name='no_breadcrumbs_fixed'),
    url(r'^no-breadcrumbs-top-nav/$',
        views.NoBreadcrumbsTopNavTemplateView.as_view(), name='no_breadcrumbs_top_nav'),
    #
    #   No Breadcrumbs, No Footer
    #
    url(r'^no-breadcrumbs-footer-boxed/$',
        views.NoBreadcrumbsFooterBoxedTemplateView.as_view(), name='no_breadcrumbs_footer_boxed'),
    url(r'^no-breadcrumbs-footer-collapsed/$',
        views.NoBreadcrumbsFooterCollapsedTemplateView.as_view(), name='no_breadcrumbs_footer_collapsed'),
    url(r'^no-breadcrumbs-footer-fixed/$',
        views.NoBreadcrumbsFooterFixedTemplateView.as_view(), name='no_breadcrumbs_footer_fixed'),
    url(r'^no-breadcrumbs-footer-top-nav/$',
        views.NoBreadcrumbsFooterTopNavTemplateView.as_view(), name='no_breadcrumbs_footer_top_nav'),
    #
    #   No Content Header
    #
    url(r'^no-content-header-boxed/$',
        views.NoContentHeaderBoxedTemplateView.as_view(), name='no_content_header_boxed'),
    url(r'^no-content-header-collapsed/$',
        views.NoContentHeaderCollapsedTemplateView.as_view(), name='no_content_header_collapsed'),
    url(r'^no-content-header-fixed/$',
        views.NoContentHeaderFixedTemplateView.as_view(), name='no_content_header_fixed'),
    url(r'^no-content-header-top-nav/$',
        views.NoContentHeaderTopNavTemplateView.as_view(), name='no_content_header_top_nav'),
    #
    #   No Footer
    #
    url(r'^no-footer-boxed/$',
        views.NoFooterBoxedTemplateView.as_view(), name='no_footer_boxed'),
    url(r'^no-footer-collapsed/$',
        views.NoFooterCollapsedTemplateView.as_view(), name='no_footer_collapsed'),
    url(r'^no-footer-fixed/$',
        views.NoFooterFixedTemplateView.as_view(), name='no_footer_fixed'),
    url(r'^no-footer-top-nav/$',
        views.NoFooterTopNavTemplateView.as_view(), name='no_footer_top_nav'),
]
