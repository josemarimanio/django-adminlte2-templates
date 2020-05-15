#
#   HTML
#

ADMINLTE_HTML_LANG = 'en-us'
"""
    *(str)* HTML 'lang' attribute value.

    Defaults to ``'en-us'``
"""

ADMINLTE_HTML_LANG_BIDI = 'ltr'
"""
    *(str)* HTML ``dir`` attribute value for handling bidirectional text. 
    
    Valid values are ``'ltr'``, ``'rtl'``, ``'auto'``.
    
    Defaults to ``'ltr'``.
"""

ADMINLTE_USE_SHIM = False
"""
    *(bool)* Toggle to use HTML5 Shim for IE9 support.

    Defaults to ``False``.
"""

#
#   Skin theme
#

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

#
#   Control theme
#

# Valid AdminLTE control sidebar style values
CONTROL_STYLE_DARK = 'control-sidebar-dark'
CONTROL_STYLE_LIGHT = 'control-sidebar-light'
CONTROL_STYLE_CHOICES = (CONTROL_STYLE_DARK, CONTROL_STYLE_LIGHT)

ADMINLTE_CONTROL_STYLE = CONTROL_STYLE_DARK
"""
    *(str)* Default AdminLTE control sidebar style.

    Valid values are: ``'control-sidebar-dark'``, ``'control-sidebar-light'``.

    Defaults to ``'control-sidebar-dark'``.
"""

#
#   CDN
#

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
    SKIN_STYLE_BLACK: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-black.min.css',
    SKIN_STYLE_BLACK_LIGHT: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-black-light.min.css',
    SKIN_STYLE_BLUE: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-blue.min.css',
    SKIN_STYLE_BLUE_LIGHT: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-blue-light.min.css',
    SKIN_STYLE_GREEN: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-green.min.css',
    SKIN_STYLE_GREEN_LIGHT: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-green-light.min.css',
    SKIN_STYLE_PURPLE: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-purple.min.css',
    SKIN_STYLE_PURPLE_LIGHT: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-purple-light.min.css',
    SKIN_STYLE_RED: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-red.min.css',
    SKIN_STYLE_RED_LIGHT: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-red-light.min.css',
    SKIN_STYLE_YELLOW: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-yellow.min.css',
    SKIN_STYLE_YELLOW_LIGHT: 'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.4.18/css/skins/skin-yellow-light.min.css',
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

ADMINLTE_CDN_DATATABLES_CSS_CORE = 'https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css'
"""
    *(str)* CDN link for DataTables 1.10.21 core CSS file.

    Defaults to ``'https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css'``.
"""

ADMINLTE_CDN_DATATABLES_JS_CORE = 'https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js'
"""
    *(str)* CDN link for DataTables 1.10.21 core JS file.
    
    Defaults to ``'https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js'``.
"""

ADMINLTE_CDN_FONTAWESOME_CSS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
"""
    *(str)* CDN link for Font-Awesome 4.7.0 core CSS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'``.
"""

ADMINLTE_CDN_JQUERY_JS_CORE = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js'
"""
    *(str)* CDN link for jQuery 3.5.1 JS file.

    Defaults to ``'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js'``.
"""

ADMINLTE_CDN_HTML5SHIV_JS_CORE = 'https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js'
"""
    *(str)* CDN link for HTML5 Shim script HTML5 Shiv JS file.

    Defaults to ``'https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js'``.
"""

ADMINLTE_CDN_RESPOND_JS_CORE = 'https://oss.maxcdn.com/respond/1.4.2/respond.min.js'
"""
    *(str)* CDN link for HTML5 Shim script Respond JS file.

    Defaults to ``'https://oss.maxcdn.com/respond/1.4.2/respond.min.js'``.
"""

ADMINLTE_CDN_SELECT2_JS_CORE = 'https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/js/select2.min.js'
"""
    *(str)* CDN link for Select2 4.0.13 core JS file
    
    Defaults to ``'https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/js/select2.min.js'``.
"""

ADMINLTE_CDN_SELECT2_CSS_CORE = 'https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/css/select2.min.css'
"""
    *(str)* CDN link for Select2 4.0.13 core CSS file
    
    Defaults to ``'https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/css/select2.min.css'``.
"""

#
#   Footer
#
ADMINLTE_FOOTER_VERSION = '1.0.0'
"""
    *(str)* Footer version number text, defaults to ``'1.0.0'``.
"""

#
#   Gravatar
#

# Valid Gravatar 'default' parameter values
GRAVATAR_DEFAULT_404 = '404'
GRAVATAR_DEFAULT_MP = 'mp'
GRAVATAR_DEFAULT_IDENTICON = 'identicon'
GRAVATAR_DEFAULT_MONSTERID = 'monsterid'
GRAVATAR_DEFAULT_WAVATAR = 'wavatar'
GRAVATAR_DEFAULT_RETRO = 'retro'
GRAVATAR_DEFAULT_ROBOHASH = 'robohash'
GRAVATAR_DEFAULT_BLANK = 'blank'
GRAVATAR_DEFAULT_CHOICES = (GRAVATAR_DEFAULT_404, GRAVATAR_DEFAULT_MP, GRAVATAR_DEFAULT_IDENTICON,
                            GRAVATAR_DEFAULT_MONSTERID, GRAVATAR_DEFAULT_WAVATAR, GRAVATAR_DEFAULT_RETRO,
                            GRAVATAR_DEFAULT_ROBOHASH, GRAVATAR_DEFAULT_BLANK)

# Valid Gravatar 'rating' parameter values
GRAVATAR_RATING_G = 'g'
GRAVATAR_RATING_PG = 'pg'
GRAVATAR_RATING_R = 'r'
GRAVATAR_RATING_X = 'x'
GRAVATAR_RATING_CHOICES = (GRAVATAR_RATING_G, GRAVATAR_RATING_PG, GRAVATAR_RATING_R, GRAVATAR_RATING_X)

# Valid Gravatar 'size' range
GRAVATAR_SIZE_MINIMUM = 1
GRAVATAR_SIZE_MAXIMUM = 2048

ADMINLTE_GRAVATAR_SIZE = 80
"""
    *(int)* Default Gravatar image size.

    You may request images anywhere from ``1`` up to ``2048``, however note that many users have lower 
    resolution images, so requesting larger sizes may result in pixelation/low-quality images.

    Defaults to ``80``. 
"""

ADMINLTE_GRAVATAR_DEFAULT = GRAVATAR_DEFAULT_MP
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

ADMINLTE_GRAVATAR_RATING = GRAVATAR_RATING_PG
"""
    *(str)* Gravatar image rating.

    Valid values are: ``'g'``, ``'pg'``, ``'r'``, ``'x'``.

    Defaults to ``'pg'``.
"""

#
#   Layouts
#
_LAYOUT_BOXED_FILENAME = 'boxed.html'
_LAYOUT_COLLAPSED_FILENAME = 'collapsed_sidebar.html'
_LAYOUT_FIXED_FILENAME = 'fixed.html'
_LAYOUT_TOP_NAV_FILENAME = 'top_navigation.html'
_LAYOUT_DEFAULT_DIRECTORY = 'adminlte2/layouts/'
_LAYOUT_BAREBONES_DIRECTORY = 'adminlte2/shortcuts/barebones/'
_LAYOUT_NO_BREADCRUMBS_DIRECTORY = 'adminlte2/shortcuts/no_breadcrumbs/'
_LAYOUT_NO_BREADCRUMBS_FOOTER_DIRECTORY = 'adminlte2/shortcuts/no_breadcrumbs_footer/'
_LAYOUT_NO_FOOTER_DIRECTORY = 'adminlte2/shortcuts/no_footer/'
_LAYOUT_NO_CONTENT_HEADER = 'adminlte2/shortcuts/no_content_header/'
# Default
LAYOUT_DEFAULT_BOXED = _LAYOUT_DEFAULT_DIRECTORY + _LAYOUT_BOXED_FILENAME
LAYOUT_DEFAULT_COLLAPSED = _LAYOUT_DEFAULT_DIRECTORY + _LAYOUT_COLLAPSED_FILENAME
LAYOUT_DEFAULT_FIXED = _LAYOUT_DEFAULT_DIRECTORY + _LAYOUT_FIXED_FILENAME
LAYOUT_DEFAULT_LOGIN = _LAYOUT_DEFAULT_DIRECTORY + 'login.html'
LAYOUT_DEFAULT_REGISTER = _LAYOUT_DEFAULT_DIRECTORY + 'register.html'
LAYOUT_DEFAULT_TOP_NAV = _LAYOUT_DEFAULT_DIRECTORY + _LAYOUT_TOP_NAV_FILENAME
# Barebones
LAYOUT_BAREBONES_BOXED = _LAYOUT_BAREBONES_DIRECTORY + _LAYOUT_BOXED_FILENAME
LAYOUT_BAREBONES_COLLAPSED = _LAYOUT_BAREBONES_DIRECTORY + _LAYOUT_COLLAPSED_FILENAME
LAYOUT_BAREBONES_FIXED = _LAYOUT_BAREBONES_DIRECTORY + _LAYOUT_FIXED_FILENAME
LAYOUT_BAREBONES_TOP_NAV = _LAYOUT_BAREBONES_DIRECTORY + _LAYOUT_TOP_NAV_FILENAME
# No Breadcrumbs
LAYOUT_NO_BREADCRUMBS_BOXED = _LAYOUT_NO_BREADCRUMBS_DIRECTORY + _LAYOUT_BOXED_FILENAME
LAYOUT_NO_BREADCRUMBS_COLLAPSED = _LAYOUT_NO_BREADCRUMBS_DIRECTORY + _LAYOUT_COLLAPSED_FILENAME
LAYOUT_NO_BREADCRUMBS_FIXED = _LAYOUT_NO_BREADCRUMBS_DIRECTORY + _LAYOUT_FIXED_FILENAME
LAYOUT_NO_BREADCRUMBS_TOP_NAV = _LAYOUT_NO_BREADCRUMBS_DIRECTORY + _LAYOUT_TOP_NAV_FILENAME
# No Breadcrumbs, No Footer
LAYOUT_NO_BREADCRUMBS_FOOTER_BOXED = _LAYOUT_NO_BREADCRUMBS_FOOTER_DIRECTORY + _LAYOUT_BOXED_FILENAME
LAYOUT_NO_BREADCRUMBS_FOOTER_COLLAPSED = _LAYOUT_NO_BREADCRUMBS_FOOTER_DIRECTORY + _LAYOUT_COLLAPSED_FILENAME
LAYOUT_NO_BREADCRUMBS_FOOTER_FIXED = _LAYOUT_NO_BREADCRUMBS_FOOTER_DIRECTORY + _LAYOUT_FIXED_FILENAME
LAYOUT_NO_BREADCRUMBS_FOOTER_TOP_NAV = _LAYOUT_NO_BREADCRUMBS_FOOTER_DIRECTORY + _LAYOUT_TOP_NAV_FILENAME
# No Content Header
LAYOUT_NO_CONTENT_HEADER_BOXED = _LAYOUT_NO_CONTENT_HEADER + _LAYOUT_BOXED_FILENAME
LAYOUT_NO_CONTENT_HEADER_COLLAPSED = _LAYOUT_NO_CONTENT_HEADER + _LAYOUT_COLLAPSED_FILENAME
LAYOUT_NO_CONTENT_HEADER_FIXED = _LAYOUT_NO_CONTENT_HEADER + _LAYOUT_FIXED_FILENAME
LAYOUT_NO_CONTENT_HEADER_TOP_NAV = _LAYOUT_NO_CONTENT_HEADER + _LAYOUT_TOP_NAV_FILENAME
# No Footer
LAYOUT_NO_FOOTER_BOXED = _LAYOUT_NO_FOOTER_DIRECTORY + _LAYOUT_BOXED_FILENAME
LAYOUT_NO_FOOTER_COLLAPSED = _LAYOUT_NO_FOOTER_DIRECTORY + _LAYOUT_COLLAPSED_FILENAME
LAYOUT_NO_FOOTER_FIXED = _LAYOUT_NO_FOOTER_DIRECTORY + _LAYOUT_FIXED_FILENAME
LAYOUT_NO_FOOTER_TOP_NAV = _LAYOUT_NO_FOOTER_DIRECTORY + _LAYOUT_TOP_NAV_FILENAME

#
#   Static files
#
ADMINLTE_STATIC_ENABLE_DATATABLES = True
"""
    *(bool)* Toggle to enable the Datatables library (https://www.datatables.net/) included out-of-the-box.
    
    Defaults to ``True``.
"""

ADMINLTE_STATIC_ENABLE_FONTAWESOME = True
"""
    *(bool)* Toggle to enable the Font Awesome library (https://fontawesome.com/v4.7.0/icons/) included out-of-the-box.
    
    Defaults to ``True``.
"""

ADMINLTE_STATIC_ENABLE_SELECT2 = True
"""
    *(bool)* Toggle to enable the Select2 library (https://select2.org/) included out-of-the-box.
    
    Defaults to ``True``.
"""

#
#   Paginator
#
PAGINATOR_ALIGN_INITIAL = 'initial'
PAGINATOR_ALIGN_CENTER = 'center'
PAGINATOR_ALIGN_LEFT = 'left'
PAGINATOR_ALIGN_RIGHT = 'right'
PAGINATOR_ALIGN_CHOICES = (PAGINATOR_ALIGN_INITIAL, PAGINATOR_ALIGN_CENTER, PAGINATOR_ALIGN_LEFT, PAGINATOR_ALIGN_RIGHT)
PAGINATOR_TEMPLATE_NAME = 'adminlte2/extras/paginator.html'

#
#   Page title
#

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
