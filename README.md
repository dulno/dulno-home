<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/logo-light.webp">
    <img src=".github/logo-dark.webp" alt="Dulno logo" width="128">
  </picture>

  <h1><b>Dulno - Home</b><br><br></h1>

</div>

This project implements the homepage of Dulno. This includes general information and, among other things, the landing page and the price page.

## Status

|      | Pipeline status                                                       |
|------|-----------------------------------------------------------------------|
| main | ![](https://github.com/dulno/dulno-home/actions/workflows/ci.yml/badge.svg?branch=main)  |

## Installation

```bash
python -m venv env

source env/bin/activate

pip install gunicorn -r requirements.txt

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

## License

© Dulno. Licensed under [CC BY-NC-SA 4.0](LICENSE): free for non-commercial use with attribution to Dulno, modifications must be shared under the same license. Third-party code (e.g. under `static/dependency/`) keeps its own license.
