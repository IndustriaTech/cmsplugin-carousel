import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'example/media_files/')
