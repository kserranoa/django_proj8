import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_CONNECTION = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'karinaDelicia',
        'USER': 'postgres',
        'PASSWORD': '76543210',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}