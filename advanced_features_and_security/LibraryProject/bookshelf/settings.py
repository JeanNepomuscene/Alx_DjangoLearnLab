INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # if you have other apps
    'advanced_features_and_security',  # your app containing CustomUser
]

# Use custom user model
AUTH_USER_MODEL = 'advanced_features_and_security.CustomUser'
AUTH_USER_MODEL = "bookshelf.CustomUser"
