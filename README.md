# Installation

```
$ git clone https://github.com/kursadbilgin/randomuser.git
$ cd randomuser
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Add database information of your settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'host',
        'PORT': 'port',
    }
}
```

# Running

```
$ python manage.py runserver
```

# User create command

```
$ python manage.py create_user_command 5000
```

