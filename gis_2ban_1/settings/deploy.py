from .base import *

# env_list = dict()
#
# local_env = open(os.path.join(BASE_DIR, '.env'))
#
# while True:
#     line = local_env.readline()
#     if not line:
#         break
#     line = line.replace('\n', '')
#     start = line.find('=')
#     key = line[:start]
#     value = line[start+1:]
#     env_list[key] = value


def read_secret(secret_name):
    with open('/run/secrets/' + secret_name) as f:
        secret = f.read()
        secret = secret.rstrip().lstrip()
    return secret

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env_list['SECRET_KEY']
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# * : 모든 외부 호스트를 다 허용해줌
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}