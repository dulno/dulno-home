ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN ln -s /obfuscation /dulno

COPY . /dulno

WORKDIR /dulno

ENV OBFUSCATION_HOME=/dulno

RUN node obfuscation/obfuscate.js

FROM python:3.13-slim

# Install dependencies & fix CVE-2024-56406 by updating perl-base
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        perl-base=5.36.0-7+deb12u2 \
        gettext \
        linux-libc-dev \
        curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir django gunicorn django-cors-headers requests jwt

WORKDIR /app

COPY --from=builder /dulno/. /app/

RUN ls -R .

RUN python dulno/manage.py compilemessages

ENTRYPOINT ["gunicorn", "--config", "dulno/app/gunicorn-config.py", "app.wsgi"]