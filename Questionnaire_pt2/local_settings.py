SECRET_KEY = 'zq4f+jyjl=en=a@-7&-$k)!&o=r_wv81#obd72s-c0dh+2l$x0hello'
ALLOWED_HOSTS = ['67.205.181.154']

DATABASES = {
    'default': {
        #SqLite
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #Postgres
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'alltogether',
        'USER': 'aditya',
        'PASSWORD': 'Warmachine@42',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True
