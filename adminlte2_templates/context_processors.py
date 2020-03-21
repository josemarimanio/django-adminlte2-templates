from django.conf import settings


def template(request):
    """
        Get all settings related to the AdminLTE 2 module and
        return them as context variables
    """
    context = {}

    # Skin style color. Valid values are:
    #   skin-black, skin-black-light, skin-blue, skin-blue-light, skin-green, skin-green-light, skin-purple,
    #   skin-purple-light, skin-red, skin-red-light, skin-yellow, skin-yellow-light
    try:
        context['ADMINLTE_SKIN_STYLE'] = settings.ADMINLTE_SKIN_STYLE
    except AttributeError:
        context['ADMINLTE_SKIN_STYLE'] = 'skin-blue'

    return context
