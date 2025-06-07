ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-web-obfuscation:latest AS builder

RUN mkdir -p /dulno && cp -a /obfuscation /dulno/

COPY static /dulno/static
COPY obfuscation /dulno/obfuscation

ENV OBFUSCATION_HOME=/dulno

RUN node /dulno/obfuscation/obfuscate.js

FROM ${DOCKER_REGISTRY}/dulno-web-proxy:latest

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

COPY --from=builder /dulno/static /dulno/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN mkdir -p /etc/nginx/sites-enabled
RUN cp /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]