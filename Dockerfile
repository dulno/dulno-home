ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web-obfuscation:latest AS builder

COPY . /dulno

RUN ls -R /dulno

WORKDIR /dulno

ENV OBFUSCATION_HOME=/dulno

RUN node obfuscation/obfuscate.js

FROM ${DOCKER_REGISTRY}/dulno-web-base:latest

COPY --from=builder /dulno/manage.py /dulno/manage.py
COPY --from=builder /dulno/templates/ /dulno/templates/
COPY --from=builder /dulno/locale/ /dulno/locale/
COPY --from=builder /dulno/home/ /dulno/home/
COPY --from=builder /dulno/errors/ /dulno/errors/
COPY --from=builder /dulno/base/ /dulno/base/
COPY --from=builder /dulno/app/ /dulno/app/

WORKDIR /dulno

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]