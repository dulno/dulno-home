ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web-obfuscation:latest AS builder

COPY templates/ /dulno/templates/
COPY home/ /dulno/home/
COPY errors/ /dulno/errors/
COPY base/ /dulno/base/
COPY obfuscation/ /dulno/obfuscation/

ENV OBFUSCATION_HOME=/dulno

RUN node /dulno/obfuscation/obfuscate.js

FROM ${DOCKER_REGISTRY}/dulno-web-base:latest

COPY manage.py /dulno/manage.py
COPY locale/ /dulno/locale/
COPY app/ /dulno/app/
COPY --from=builder /dulno/templates/ /dulno/templates/
COPY --from=builder /dulno/home/ /dulno/home/
COPY --from=builder /dulno/errors/ /dulno/errors/
COPY --from=builder /dulno/base/ /dulno/base/

WORKDIR /dulno

COPY requirements.txt /dulno/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt

RUN django-admin compilemessages

USER 1000

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]