from django.conf import settings
from adminlte2_templates import constants


def _get_context(context):
    """
        Return the context from Django settings.
        If no context is found, get default value from module constants
    """
    return getattr(settings, context, getattr(constants, context))


def template(request):
    """
        Get all settings related to the AdminLTE 2 module and return them as context variables
    """
    skin_style = _get_context('ADMINLTE_SKIN_STYLE')

    context = {
        'DEBUG': getattr(settings, 'DEBUG'),

        #
        # HTML 'lang' attribute value
        #
        'ADMINLTE_HTML_LANG': _get_context('ADMINLTE_HTML_LANG'),

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
        'ADMINLTE_CONTROL_STYLE': _get_context('ADMINLTE_CONTROL_STYLE'),

        #
        # Toggle to use HTML5 Shim
        #
        'ADMINLTE_USE_SHIM': _get_context('ADMINLTE_USE_SHIM'),

        #
        # Toggle to use CDN for AdminLTE dependencies
        #
        'ADMINLTE_USE_CDN': _get_context('ADMINLTE_USE_CDN'),

        #
        # Dependency CDN URLs
        #
        # AdminLTE 2.4.18
        'ADMINLTE_CDN_ADMINLTE_CSS_CORE': _get_context('ADMINLTE_CDN_ADMINLTE_CSS_CORE'),
        'ADMINLTE_CDN_ADMINLTE_CSS_SKIN': _get_context('ADMINLTE_CDN_ADMINLTE_CSS_SKIN')[skin_style],
        'ADMINLTE_CDN_ADMINLTE_JS_CORE': _get_context('ADMINLTE_CDN_ADMINLTE_JS_CORE'),
        # Bootstrap 3.4.1
        'ADMINLTE_CDN_BOOTSTRAP_CSS_CORE': _get_context('ADMINLTE_CDN_BOOTSTRAP_CSS_CORE'),
        'ADMINLTE_CDN_BOOTSTRAP_JS_CORE': _get_context('ADMINLTE_CDN_BOOTSTRAP_JS_CORE'),
        # Font-Awesome 4.7.0
        'ADMINLTE_CDN_FONTAWESOME_CSS_CORE': _get_context('ADMINLTE_CDN_FONTAWESOME_CSS_CORE'),
        # jQuery 3.4.1
        'ADMINLTE_CDN_JQUERY_JS_CORE': _get_context('ADMINLTE_CDN_JQUERY_JS_CORE'),
        # Shims
        'ADMINLTE_CDN_HTML5SHIV_CORE_JS': _get_context('ADMINLTE_CDN_HTML5SHIV_CORE_JS'),
        'ADMINLTE_CDN_RESPOND_CORE_JS': _get_context('ADMINLTE_CDN_RESPOND_CORE_JS'),
    }

    return context
