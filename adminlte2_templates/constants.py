ADMINLTE_HTML_LANG = 'en-us'
"""
    *(str)* HTML 'lang' attribute value.

    Defaults to ``'en-us'``
"""

ADMINLTE_USE_SHIM = False
"""
    *(bool)* Toggle to use HTML5 Shim for IE9 support.

    Defaults to ``False``.
"""

ADMINLTE_USE_CDN = False
"""
    *(bool)* Toggle to use CDN links for AdminLTE dependencies.

    Defaults to ``False``.
"""

ADMINLTE_CDN_ADMINLTE_CSS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/AdminLTE.min.css'
"""
    *(str)* CDN link for AdminLTE 2.4.18 core CSS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/AdminLTE.min.css'``.
"""

ADMINLTE_CDN_ADMINLTE_CSS_SKIN = {
    'skin-black': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-black.min.css',
    'skin-black-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-black-light.min.css',
    'skin-blue': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-blue.min.css',
    'skin-blue-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-blue-light.min.css',
    'skin-green': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-green.min.css',
    'skin-green-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-green-light.min.css',
    'skin-purple': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-purple.min.css',
    'skin-purple-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-purple-light.min.css',
    'skin-red': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-red.min.css',
    'skin-red-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-red-light.min.css',
    'skin-yellow': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-yellow.min.css',
    'skin-yellow-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-yellow-light.min.css',
}
"""
    *(dict)* CDN links for AdminLTE 2.4.18 skin CSS files.

    Valid keys are: ``'skin-black'``, ``'skin-black-light'``, ``'skin-blue'``, ``'skin-blue-light'``,
    ``'skin-green'``, ``'skin-green-light'``, ``'skin-purple'``, ``'skin-purple-light'``,
    ``'skin-red'``, ``'skin-red-light'``, ``'skin-yellow'``, ``'skin-yellow-light'``.

    Default:

    .. code:: python

        {
            'skin-black': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-black.min.css',
            'skin-black-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-black-light.min.css',
            'skin-blue': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-blue.min.css',
            'skin-blue-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-blue-light.min.css',
            'skin-green': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-green.min.css',
            'skin-green-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-green-light.min.css',
            'skin-purple': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-purple.min.css',
            'skin-purple-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-purple-light.min.css',
            'skin-red': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-red.min.css',
            'skin-red-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-red-light.min.css',
            'skin-yellow': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-yellow.min.css',
            'skin-yellow-light': 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-yellow-light.min.css',
        }
"""

ADMINLTE_CDN_ADMINLTE_JS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/js/adminlte.min.js'
"""
    *(str)* CDN link for AdminLTE 2.4.18 core JS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/js/adminlte.min.js'``.
"""

ADMINLTE_CDN_BOOTSTRAP_CSS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css'
"""
    *(str)* CDN link for Bootstrap 3.4.1 core CSS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css'``.
"""

ADMINLTE_CDN_BOOTSTRAP_JS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js'
"""
    *(str)* CDN link for Bootstrap 3.4.1 core JS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js'``.
"""

ADMINLTE_CDN_FONTAWESOME_CSS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
"""
    *(str)* CDN link for Font-Awesome 4.7.0 core CSS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'``.
"""

ADMINLTE_CDN_JQUERY_JS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js'
"""
    *(str)* CDN link for jQuery 3.4.1 JS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js'``.
"""

ADMINLTE_CDN_HTML5SHIV_CORE_JS = 'https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js'
"""
    *(str)* CDN link for HTML5 Shim script HTML5 Shiv JS file.

    Defaults to ``https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js``.
"""

ADMINLTE_CDN_RESPOND_CORE_JS = 'https://oss.maxcdn.com/respond/1.4.2/respond.min.js'
"""
    *(str)* CDN link for HTML5 Shim script Respond JS file.

    Defaults to ``https://oss.maxcdn.com/respond/1.4.2/respond.min.js``.
"""

# Valid AdminLTE skin style values
SKIN_STYLE_BLACK = 'skin-black'
SKIN_STYLE_BLACK_LIGHT = 'skin-black-light'
SKIN_STYLE_BLUE = 'skin-blue'
SKIN_STYLE_BLUE_LIGHT = 'skin-blue-light'
SKIN_STYLE_GREEN = 'skin-green'
SKIN_STYLE_GREEN_LIGHT = 'skin-green-light'
SKIN_STYLE_PURPLE = 'skin-purple'
SKIN_STYLE_PURPLE_LIGHT = 'skin-purple-light'
SKIN_STYLE_RED = 'skin-red'
SKIN_STYLE_RED_LIGHT = 'skin-red-light'
SKIN_STYLE_YELLOW = 'skin-yellow'
SKIN_STYLE_YELLOW_LIGHT = 'skin-yellow-light'
SKIN_STYLE_CHOICES = (SKIN_STYLE_BLACK, SKIN_STYLE_BLACK_LIGHT, SKIN_STYLE_BLUE, SKIN_STYLE_BLUE_LIGHT,
                      SKIN_STYLE_GREEN, SKIN_STYLE_GREEN_LIGHT, SKIN_STYLE_PURPLE, SKIN_STYLE_PURPLE_LIGHT,
                      SKIN_STYLE_RED, SKIN_STYLE_RED_LIGHT, SKIN_STYLE_YELLOW, SKIN_STYLE_YELLOW_LIGHT)

ADMINLTE_SKIN_STYLE = SKIN_STYLE_BLUE
"""
    *(str)* Default AdminLTE skin style.

    Valid values are: ``'skin-black'``, ``'skin-black-light'``, ``'skin-blue'``, ``'skin-blue-light'``,
    ``'skin-green'``, ``'skin-green-light'``, ``'skin-purple'``, ``'skin-purple-light'``,
    ``'skin-red'``, ``'skin-red-light'``, ``'skin-yellow'``, ``'skin-yellow-light'``.

    Defaults to ``'skin-blue'``.
"""

CONTROL_STYLE_DARK = 'control-sidebar-dark'
CONTROL_STYLE_LIGHT = 'control-sidebar-light'
CONTROL_STYLE_CHOICES = (CONTROL_STYLE_DARK, CONTROL_STYLE_LIGHT)

ADMINLTE_CONTROL_STYLE = CONTROL_STYLE_DARK
"""
    *(str)* Default AdminLTE control sidebar style.

    Valid values are: ``'control-sidebar-dark'``, ``'control-sidebar-light'``.

    Defaults to ``'control-sidebar-dark'``.
"""

ADMINLTE_GRAVATAR_SIZE = 80
"""
    *(int)* Default Gravatar image size.

    You may request images anywhere from ``1`` up to ``2048``, however note that many users have lower 
    resolution images, so requesting larger sizes may result in pixelation/low-quality images.

    Defaults to ``80``. 
"""

ADMINLTE_GRAVATAR_DEFAULT = 'mp'
"""
    *(str)* Default Gravatar image to load.

    You can supply your own default image by supplying the URL to an image. Alternatively, you can use any of these
    valid values: ``'404'``, ``'mp'``, ``'identicon'``, ``'monsterid'``, ``'wavatar'``, ``'retro'``, 
    ``'robohash'``, ``'blank'``.

    Defaults to ``'mp'``.
"""

ADMINLTE_GRAVATAR_FORCE_DEFAULT = False
"""
    *(bool)* Toggle to force load the default Gravatar image.

    Defaults to ``False``.
"""

ADMINLTE_GRAVATAR_RATING = 'pg'
"""
    *(str)* Gravatar image rating.

    Valid values are: ``'g'``, ``'pg'``, ``'r'``, ``'x'``.

    Defaults to ``'pg'``.
"""

ADMINLTE_TITLE_FORMAT = '{site} {divider} {page}'
"""
    *(str)* Page title string format.
    
    Supported string format parameters are:
    
    - **site**: Site name
    - **divider**: Divider character between the site name and current page name
    - **page**: Current page name
    
    Defaults to ``'{site} {divider} {page}'``.
"""

ADMINLTE_TITLE_FORMAT_PAGINATION = '{site} {divider} {page} ({curr_no} of {last_no})'
"""
    *(str)* Page title string format for pages with pagination (ListView, etc.)
    
    Supported string format parameters are:
    
    - **site**: Site name
    - **divider**: Divider character between the site name and current page name
    - **page**: Current page name
    - **curr_no**: Current page number
    - **last_no**: Last page number
    
    Defaults to ``'{site} {divider} {page} ({curr_no} of {last_no})'``.
"""

ADMINLTE_TITLE_SITE = 'AdminLTE'
"""
    *(str)* Page title site name text.
    
    Defaults to ``'AdminLTE'``.
"""

ADMINLTE_TITLE_DIVIDER = '|'
"""
    *(str)* Page title divider for page name and site name.
    
    Defaults to ``'|'``.
"""
