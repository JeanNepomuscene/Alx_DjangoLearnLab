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
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["yourdomain.com", "127.0.0.1"]  # adjust as needed

# Browser security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True

# Cookie security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Content Security Policy (basic)
# If django-csp is installed, add to INSTALLED_APPS and MIDDLEWARE
# Otherwise set manually in middleware or views
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com")
CSP_SCRIPT_SRC = ("'self'", "https://cdn.jsdelivr.net")

# Recommended: use django.middleware.security.SecurityMiddleware first
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # If using django-csp
    # "csp.middleware.CSPMiddleware",
]

