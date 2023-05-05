DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tmp/db.sqlite3',
    }
}

CELERY_BROKER_URL = 'amqp://{0}:{1}@{2}:{3}//'.format(
    os.environ['RABBITMQ_DEFAULT_USER'],
    os.environ['RABBITMQ_DEFAULT_PASS'],
    os.getenv('RABBITMQ_DEFAULT_HOST', '127.0.0.1'),
    os.getenv('RABBITMQ_DEFAULT_PORT', '5672'),
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}
