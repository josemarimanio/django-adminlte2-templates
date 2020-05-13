from django.conf import settings

from adminlte2_templates.core import get_settings


def template(request):
    """
        Get all settings related to the AdminLTE 2 module and return them as context variables
    """
    skin_style = get_settings('ADMINLTE_SKIN_STYLE')

    context = {
        'DEBUG': getattr(settings, 'DEBUG'),

        #
        # Footer version value
        #
        'ADMINLTE_FOOTER_VERSION': get_settings('ADMINLTE_FOOTER_VERSION'),

        #
        # HTML 'lang' attribute value
        #
        'ADMINLTE_HTML_LANG': get_settings('ADMINLTE_HTML_LANG', django_setting='LANGUAGE_CODE'),

        #
        # HTML 'dir' attribute value
        #
        'ADMINLTE_HTML_LANG_BIDI': get_settings('ADMINLTE_HTML_LANG_BIDI'),

        #
        # Skin style color. Valid values are:
        #   skin-black, skin-black-light, skin-blue, skin-blue-light, skin-green, skin-green-light, skin-purple,
        #   skin-purple-light, skin-red, skin-red-light, skin-yellow, skin-yellow-light
        #
        'ADMINLTE_SKIN_STYLE': skin_style,

        #
        # Control sidebar color. Valid values are:
        #   control-sidebar-dark, control-sidebar-light
        #
        'ADMINLTE_CONTROL_STYLE': get_settings('ADMINLTE_CONTROL_STYLE'),

        #
        # Toggle to enable optional static libraries
        #
        'ADMINLTE_STATIC_ENABLE_DATATABLES': get_settings('ADMINLTE_STATIC_ENABLE_DATATABLES'),
        'ADMINLTE_STATIC_ENABLE_FONTAWESOME': get_settings('ADMINLTE_STATIC_ENABLE_FONTAWESOME'),
        'ADMINLTE_STATIC_ENABLE_SELECT2': get_settings('ADMINLTE_STATIC_ENABLE_SELECT2'),

        #
        # Toggle to use HTML5 Shim
        #
        'ADMINLTE_USE_SHIM': get_settings('ADMINLTE_USE_SHIM'),

        #
        # Toggle to use CDN for AdminLTE dependencies
        #
        'ADMINLTE_USE_CDN': get_settings('ADMINLTE_USE_CDN'),
    }

    if context['ADMINLTE_USE_CDN']:
        #
        # Dependency CDN URLs
        #
        context.update({
            # AdminLTE 2.4.18
            'ADMINLTE_CDN_ADMINLTE_CSS_CORE': get_settings('ADMINLTE_CDN_ADMINLTE_CSS_CORE'),
            'ADMINLTE_CDN_ADMINLTE_CSS_SKIN': get_settings('ADMINLTE_CDN_ADMINLTE_CSS_SKIN')[skin_style],
            'ADMINLTE_CDN_ADMINLTE_JS_CORE': get_settings('ADMINLTE_CDN_ADMINLTE_JS_CORE'),
            # Bootstrap 3.4.1
            'ADMINLTE_CDN_BOOTSTRAP_CSS_CORE': get_settings('ADMINLTE_CDN_BOOTSTRAP_CSS_CORE'),
            'ADMINLTE_CDN_BOOTSTRAP_JS_CORE': get_settings('ADMINLTE_CDN_BOOTSTRAP_JS_CORE'),

            # jQuery 3.4.1
            'ADMINLTE_CDN_JQUERY_JS_CORE': get_settings('ADMINLTE_CDN_JQUERY_JS_CORE'),
        })

    if context['ADMINLTE_USE_CDN'] and context['ADMINLTE_USE_SHIM']:
        #
        # Shim CDN URLs
        #
        context.update({
            'ADMINLTE_CDN_HTML5SHIV_JS_CORE': get_settings('ADMINLTE_CDN_HTML5SHIV_JS_CORE'),
            'ADMINLTE_CDN_RESPOND_JS_CORE': get_settings('ADMINLTE_CDN_RESPOND_JS_CORE'),
        })

    # DataTables 1.10.21
    if context['ADMINLTE_USE_CDN'] and context['ADMINLTE_STATIC_ENABLE_DATATABLES']:
        context.update({
            'ADMINLTE_CDN_DATATABLES_CSS_CORE': get_settings('ADMINLTE_CDN_DATATABLES_CSS_CORE'),
            'ADMINLTE_CDN_DATATABLES_JS_CORE': get_settings('ADMINLTE_CDN_DATATABLES_JS_CORE'),
        })

    # Font-Awesome 4.7.0
    if context['ADMINLTE_USE_CDN'] and context['ADMINLTE_STATIC_ENABLE_FONTAWESOME']:
        context.update({
            'ADMINLTE_CDN_FONTAWESOME_CSS_CORE': get_settings('ADMINLTE_CDN_FONTAWESOME_CSS_CORE'),
        })

    # Select2 4.0.13
    if context['ADMINLTE_USE_CDN'] and context['ADMINLTE_STATIC_ENABLE_SELECT2']:
        context.update({
            'ADMINLTE_CDN_SELECT2_CSS_CORE': get_settings('ADMINLTE_CDN_SELECT2_CSS_CORE'),
            'ADMINLTE_CDN_SELECT2_JS_CORE': get_settings('ADMINLTE_CDN_SELECT2_JS_CORE'),
        })

    return context
