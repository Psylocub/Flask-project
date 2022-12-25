# Flask template project

## Local setup

**Create python environment**

```
$ python3 -m venv .venv
```

**Activate python environment**

```
$ source .venv/bin/activate
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Run database container**

```
$ docker-compose up -d db
```

**Add migrations to database**

```
$ flask db migrate
$ flask db upgrade
```

**Run application**

```
$ flask run
```

## Setup with docker

```
$ docker-compose up -d --build
```

## SMTP server setting
```
Set follow configuration in .env file: 
MAIL_SERVER, 
MAIL_PORT,
MAIL_USERNAME,
MAIL_PASSWORD.
```