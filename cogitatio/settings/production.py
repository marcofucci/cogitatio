from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Marco Fucci', 'info@marcofucci.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cogitatio',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}