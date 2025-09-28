from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-only-not-secret"
DEBUG = True
ALLOWED_HOSTS = ["*",'127.0.0.1','localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'amr_api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "amr_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "amr_project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- DRF / Auth ---
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# --- CORS/CSRF for Vite on 5173 ---
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# added by setup
CORS_ALLOWED_ORIGINS += ["http://localhost:5175"]

# added by setup
CORS_ALLOWED_ORIGINS += ["http://127.0.0.1:5175"]

CORS_ALLOW_CREDENTIALS = True
# === AMR CORS OVERRIDE (auto-appended) ===
try:
    from .local_settings import *  # noqa
except Exception:
    pass
# === END AMR CORS OVERRIDE ===

# === AUTO IMPORT LOCAL SETTINGS (AMR) ===
try:
    from .local_settings import *  # noqa
except Exception:
    pass
# === END AUTO IMPORT LOCAL SETTINGS (AMR) ===

# --- load local overrides (admin, cors, etc.) ---
try:
    from .local_settings import *
except Exception:
    pass

# === Upload limits ===
# ~10 MB in-memory parse; larger files will be streamed (tweak as needed)
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

# Render production settings
import os
import dj_database_url
from pathlib import Path

# Database configuration for Neon
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_nst1Ah7uwkER@ep-divine-darkness-adrnz69w-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... your other middleware
]

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-app.netlify.app",
]

CORS_ALLOW_ALL_ORIGINS = True  # Temporary for testing

# For Render
CSRF_TRUSTED_ORIGINS = [
    "https://biome-backend.onrender.com",
    "https://*.onrender.com",
]

# Security settings
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['*']
