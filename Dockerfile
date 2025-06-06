ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /dulno

RUN ls -R .
RUN ls -R dulno

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

COPY --from=builder /dulno /dulno

WORKDIR /dulno

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]