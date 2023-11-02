import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-sv8uxwdm^olxe6oc)aqk&zu#z-juj*tu%lw0pg#nh4c1nrola5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ENABLE_SILK = os.environ.get("ENABLE_SILK", False)

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
PROJECT_APPS = [
    "core",
    "common",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "versatileimagefield",
    "django_filters",
    "corsheaders",
]

if ENABLE_SILK:
    THIRD_PARTY_APPS += ["silk"]


INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Enable Silk middleware if ENABLE SILK is True
if ENABLE_SILK:
    MIDDLEWARE += [
        "silk.middleware.SilkyMiddleware",
    ]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# jwt configuration
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# VERSATILEIMAGEFIELD_SETTINGS = {
#     # The amount of time, in seconds, that references to created images
#     # should be stored in the cache. Defaults to `2592000` (30 days)
#     "cache_length": 2592000,
#     # The name of the cache you'd like `django-versatileimagefield` to use.
#     # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
#     # provided, the 'default' cache will be used instead.
#     "cache_name": "versatileimagefield_cache",
#     # The save quality of modified JPEG images. More info here:
#     # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
#     # Defaults to 70
#     "jpeg_resize_quality": 70,
#     # The name of the top-level folder within storage classes to save all
#     # sized images. Defaults to '__sized__'
#     "sized_directory_name": "__sized__",
#     # The name of the directory to save all filtered images within.
#     # Defaults to '__filtered__':
#     "filtered_directory_name": "__filtered__",
#     # The name of the directory to save placeholder images within.
#     # Defaults to '__placeholder__':
#     "placeholder_directory_name": "__placeholder__",
#     # Whether or not to create new images on-the-fly. Set this to `False` for
#     # speedy performance but don't forget to 'pre-warm' to ensure they're
#     # created and available at the appropriate URL.
#     "create_images_on_demand": True,
#     # A dot-notated python path string to a function that processes sized
#     # image keys. Typically used to md5-ify the 'image key' portion of the
#     # filename, giving each a uniform length.
#     # `django-versatileimagefield` ships with two post processors:
#     # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
#     #    md5 hash of `image_key`.
#     # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
#     #    of the 32 character md5 hash of `image_key`.
#     # By default, image_keys are unprocessed. To write your own processor,
#     # just define a function (that can be imported from your project's
#     # python path) that takes a single argument, `image_key` and returns
#     # a string.
#     "image_key_post_processor": None,
#     # Whether to create progressive JPEGs. Read more about progressive JPEGs
#     # here: https://optimus.io/support/progressive-jpeg/
#     "progressive_jpeg": False,
# }

# VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
#     "product_images": [
#         ("full_size", "url"),
#         ("small", "thumbnail__400x400"),
#         ("medium", "thumbnail__600x600"),
#         ("large", "thumbnail__1000x1000"),
#     ],
# }

# AUTH_USER_MODEL = 'account_api.User'

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")


# Jwt setting
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
}

PASSWORD_RESET_TIMEOUT = 900


# Cors alowed origin
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
