<div align="center">
  <img src="https://dulno.com/static/img/logo-light.webp" alt="logo" width="128"  height="auto" />

  <h1><b>Dulno - Home</b><br><br></h1>

</div>

This project implements the homepage of Dulno. This includes general information and, among other things, the landing page and the price page.

## Status

|      | Pipeline status                                                       |
|------|-----------------------------------------------------------------------|
| main | ![](https://git.dulno.com/dulno/dulno-home/badges/main/pipeline.svg)  |
| dev  | ![](https://git.dulno.com/dulno/dulno-home/badges/dev/pipeline.svg)   |

## Installation

```bash
python -m venv env

source env/bin/activate

pip install django gunicorn django-cors-headers requests jwt

django-admin compilemessages

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Run

```bash
source env/bin/activate

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Compile locales

```bash
django-admin compilemessages
```