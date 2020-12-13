# Django boilerplate (2.2)

to work faster i make this boilerplate according to my needs.

## steps

### create virtual env

```bash
virtualenv -p=python3.8 env
source env/bin/activate
cd env
mkdir src && cd src
```

### clone this repo

```bash
git clone https://github.com/mohamed17717/django-poilerplate.git .
pip install -r requirements.txt
```

then start creating your apps like normal
look in app created to use things like signals and stuff whenever you need

## contain

- [x] settings file handle static vars and templates
- [x] urls to static files
- [x] helper classes (jwt, mail)
- [x] .gitignore
- [x] signals
- [x] decorators
- [ ] most used models & views (authentication, profile, ...)
