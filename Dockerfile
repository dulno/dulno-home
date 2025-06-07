ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web:latest

RUN mkdir -p /dulno && cp -a /obfuscation /dulno/

COPY . /dulno
WORKDIR /dulno

ENV OBFUSCATION_HOME=/dulno

RUN node obfuscation/obfuscate.js

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]