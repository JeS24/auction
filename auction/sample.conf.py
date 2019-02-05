DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'auction', # name of the database
        'USER': '', # your username here
        'HOST': 'localhost',
        'PORT': '5432'
        'PASSWORD': '' # your password here
    }
}

SECRET_KEY = ''
DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', '10.1.42.56'] # modify as required

