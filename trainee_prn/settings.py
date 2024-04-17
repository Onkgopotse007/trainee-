"""
Django settings for trainee_prn project.

Generated by 'django-admin startproject' using Django 3.1.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from dotenv import load_dotenv
import os
from pathlib import Path
import sys
from django.core.management.color import color_style
import configparser
from dotenv import load_dotenv
load_dotenv()

style = color_style()

APP_NAME = 'trainee_prn'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ETC_DIR = os.path.join(BASE_DIR, 'etc')

CONFIG_FILE = f'trainee.ini'

CONFIG_PATH = os.path.join('/etc', 'trainee', CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')

# EDC SMS configuration
if 'edc_sms' in config:
    BASE_API_URL = config['edc_sms'].get('base_api_url', '')
else:
    BASE_API_URL = ''

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4gi6*1b1@pc7-uma3hd9pal-7arb(1j=u9ulwmen+9c%$^0^ay'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework.authtoken',
    'django_crypto_fields.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_sync.apps.AppConfig',
    'edc_sync_files.apps.AppConfig',
    'edc_base.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_senaite_interface.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_protocol.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'traineesubject.apps.AppConfig',
    'trainee_visit_schedule.apps.AppConfig',
    'trainee_prn.apps.EdcFacilityAppConfig',
    'trainee_prn.apps.EdcAppointmentAppConfig',
    'trainee_prn.apps.EdcVisitTrackingAppConfig',
    'trainee_prn.apps.EdcSmsAppConfig',
    'trainee_prn.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'trainee_prn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trainee_prn.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edc_trainee_db',
        'USER': 'avnadmin',
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

SITE_ID = 2

DEFAULT_STUDY_SITE = ''

DEVICE_ID = '22'
DEVICE_ROLE = ''

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

COUNTRY = 'botswana'

DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'trainee_dashboard:subject_listboard_url',
    'screening_listboard_url': 'trainee_dashboard:screening_listboard_url',
    'subject_dashboard_url': 'trainee_dashboard:subject_dashboard_url',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
