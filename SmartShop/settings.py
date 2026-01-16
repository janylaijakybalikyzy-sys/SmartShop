from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Проекттин негизги директориясы
BASE_DIR = Path(__file__).resolve().parent.parent

# Коопсуздук ачкычы
SECRET_KEY = 'django-insecure-15$16(1wrc1r3&i$fd2)en)l7i@$f+*5ll$r1s*ucv7f7obp*!'

# Иштеп чыгуу режими (Продакшнда False болушу керек)
DEBUG = True

ALLOWED_HOSTS = ['*']

# Колдонмолордун тизмеси
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products', # Сиздин тиркемеңиз
]

# Ортоңку программалар (Тил которуу үчүн LocaleMiddleware маанилүү)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Тилдерди аныктоочу механизм
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SmartShop.urls'

# Шаблондордун жөндөөсү
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # Тил өзгөрмөлөрү үчүн
                'django.template.context_processors.media', # Сүрөттөр менен иштөө үчүн
            ],
        },
    },
]

WSGI_APPLICATION = 'SmartShop.wsgi.application'

# Маалымат базасы (SQLite3 колдонулууда)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Паролду текшерүүчүлөр
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Тилдер жана локализация жөндөөлөрү
LANGUAGE_CODE = 'ky'  # Демейки тил
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Сайт колдогон тилдердин тизмеси
LANGUAGES = [
    ('ky', _('Кыргызча')),
    ('ru', _('Русский')),
    ('en', _('English')),
    ('zh-hans', _('中文 (Кытайча)')),
]

# Котормо файлдары сактала турган папка
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

# Статикалык файлдар (CSS, JS, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Бул кошулду

# Медиа файлдар (Колдонуучу тарабынан жүктөлгөн сүрөттөр)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Автоматтык ID талаасы
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'