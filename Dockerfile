ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /dulno && cp -a /obfuscation /dulno/

COPY manage.py /dulno
COPY templates /dulno/
COPY obfuscation /dulno/
COPY locale /dulno/
COPY home /dulno/
COPY errors /dulno/
COPY base /dulno/
COPY app /dulno/
WORKDIR /dulno/

ENV OBFUSCATION_HOME=/dulno

RUN node obfuscation/obfuscate.js

FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gettext && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir django gunicorn django-cors-headers requests jwt

COPY --from=builder /dulno /dulno

WORKDIR /dulno

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]