from django.contrib.messages import constants as messages

# archivo de configuración del sistema.

# versión del TP.
VERSION = 'Trabajo práctico - 1er cuatrimestre del 2024.'

# REST API de la NASA para capturar imágenes de la galería
NASA_REST_API = 'https://images-api.nasa.gov/search?q='

DEFAULT_SEARCH_WORD = 'space'

NASA_REST_API_DEFAULT_SEARCH = NASA_REST_API + DEFAULT_SEARCH_WORD


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}