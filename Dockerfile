ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web-obfuscation:latest AS builder

RUN mkdir -p /dulno && cp -a /obfuscation /dulno/

COPY . /dulno
WORKDIR /dulno

ENV OBFUSCATION_HOME=/dulno

RUN node obfuscation/obfuscate.js

FROM ${DOCKER_REGISTRY}/dulno-web-base:latest

COPY --from=builder /dulno /dulno

WORKDIR /dulno

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]