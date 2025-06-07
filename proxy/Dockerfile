ARG DOCKER_REGISTRY
ARG SERVER_NAME
FROM ${DOCKER_REGISTRY}/dulno-web-proxy:latest

ENV SERVER_NAME=${SERVER_NAME}
ENV OBFUSCATION_HOME=/dulno

RUN mkdir -p /dulno && cp -a /obfuscation /dulno/

COPY static /dulno/static
COPY obfuscation /dulno/obfuscation

RUN node /dulno/obfuscation/obfuscate.js

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN mkdir -p /etc/nginx/sites-enabled
RUN cp /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]