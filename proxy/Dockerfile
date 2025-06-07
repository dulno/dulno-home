ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web-obfuscation:latest AS builder

COPY /static/js/ /dulno/static/js/
COPY /obfuscation/ /dulno/obfuscation/

ENV OBFUSCATION_HOME=/dulno

RUN node /dulno/obfuscation/obfuscate.js

FROM ${DOCKER_REGISTRY}/dulno-web-proxy:latest

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

COPY /static/css/ /dulno/static/css/
COPY /static/img/ /dulno/static/img/
COPY /static/dependency/ /dulno/static/dependency/
COPY --from=builder /dulno/static/js/ /dulno/static/js/

RUN mkdir -p /etc/nginx/sites-enabled

COPY /proxy/nginx.conf /etc/nginx/nginx.conf
COPY /proxy/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-enabled/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-enabled/proxy && exec nginx -g 'daemon off;'"]