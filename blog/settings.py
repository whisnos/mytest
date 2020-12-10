"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!j0nnh*1$!bl1!5!)_v#6k2$p7h5g$v0+a2@psw@+vgpdjj^#)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 应用注册列表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]
# django 中间件
# django处理一个Request的过程是首先通过django 中间件，然后再通过默认的URL方式进行的。
# 所以说我们要做的就是在django 中间件这个地方把所有Request拦截住，
# 用我们自己的方式完成处理以后直接返回Response,那么我们可以简化原来的设计思路，
# 把中间件不能处理的 Request统统不管，丢给Django去处理。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'testblog',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': '127.0.0.1',
		'PORT': 3306,
	}
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# 启用密码验证
AUTH_PASSWORD_VALIDATORS = [
    {   # 检查密码和用户某些属性的相似性
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {   # 检查密码的最小长度(默认8)
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {   # 检查密码是否出现在常用密码表中
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {   # 检查密码是否全为数字
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 语言
LANGUAGE_CODE = 'en-us'
# 时区
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
