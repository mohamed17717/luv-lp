# Django Poilerplate (2.2)

to work faster i make this poilerplate according to my needs.

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
git clone ${url} .
pip install -r requirements.txt
```

then start creating your apps like normal
look in app created to use things like signals and stuff whenever you need

## contain

  [*] settings file handle static vars and templates
  [*] urls to static files
  [*] helper classes (jwt, mail)
  [*] .gitignore
  [*] signals
  [*] decorators
  [] most used models & views (authentication, profile, ...)
