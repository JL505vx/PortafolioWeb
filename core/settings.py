"""
Configuracion principal de Django para el portafolio de Jesus.

Este archivo concentra:
1) Apps instaladas.
2) Plantillas y archivos estaticos.
3) Base de datos.
4) Ajustes de seguridad para desarrollo inicial.
"""

from pathlib import Path

# BASE_DIR apunta a la raiz del proyecto (donde vive manage.py).
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta de Django. En produccion se debe mover a variable de entorno.
SECRET_KEY = 'django-insecure-xgta1^df1f3y4iz!$q5vw+8$r8*_+6*8rpoltew#av9!xxi87t'

# DEBUG True solo para desarrollo local.
DEBUG = True

# Hosts permitidos para entorno local y despliegue en Render.
ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".onrender.com"]


# Apps base de Django + app propia del portafolio.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siteapp',
]

# Middlewares en orden recomendado por Django.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Configuracion de templates:
# - DIRS agrega la carpeta templates a nivel proyecto.
# - APP_DIRS=True permite encontrar templates dentro de cada app.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Base de datos inicial con SQLite:
# ideal para arrancar rapido y validar funcionalidad.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validadores de password para el sistema de autenticacion de Django.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Config regional para Mexico.
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True

# Static files:
# - STATIC_URL: prefijo URL para estaticos.
# - STATICFILES_DIRS: carpetas locales donde estan css/js/img.
# - STATIC_ROOT: carpeta para collectstatic en produccion.
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Tipo por defecto para primary keys en modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
