"""
Configuracion principal de Django para el portafolio de Jesus.

Este archivo concentra:
1) Apps instaladas.
2) Plantillas y archivos estaticos.
3) Base de datos.
4) Ajustes de seguridad para desarrollo inicial.
"""
import os

from pathlib import Path
try:
    import dj_database_url
except ImportError:
    dj_database_url = None

# BASE_DIR apunta a la raiz del proyecto (donde vive manage.py).
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta de Django:
# - En desarrollo usa valor local por defecto.
# - En Render define SECRET_KEY en variables de entorno.
SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-key-change-me")

# DEBUG:
# - True para desarrollo local.
# - False en produccion (Render).
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Hosts permitidos:
# - Puedes pasar ALLOWED_HOSTS como csv en entorno, ej:
#   "127.0.0.1,localhost,.onrender.com"
allowed_hosts_env = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost,.onrender.com")
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(",") if host.strip()]

# Render expone este host automaticamente; lo agregamos por seguridad.
render_host = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if render_host:
    ALLOWED_HOSTS.append(render_host)


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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
# Si existe DATABASE_URL (Render + PostgreSQL), la usa.
# Si no, se queda con SQLite local.
if dj_database_url:
    DATABASES = {
        "default": dj_database_url.config(
            default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
            conn_max_age=600,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
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
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Seguridad basica para reverse proxy (Render HTTPS).
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = ["https://*.onrender.com"]
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG

# Tipo por defecto para primary keys en modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
