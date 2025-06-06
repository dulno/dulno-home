ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /dulno && cp -a /obfuscation /dulno/

COPY static /dulno/static
COPY obfuscation /dulno/obfuscation

ENV OBFUSCATION_HOME=/dulno

RUN node /dulno/obfuscation/obfuscate.js

FROM nginx:latest

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

# Fix CVE-2024-56406: Update perl-base
# Fix CVE-2025-48174: Update libavif15
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        perl-base=5.36.0-7+deb12u2 \
        libavif15=0.11.1-1+deb12u1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /dulno/static /dulno/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN mkdir -p /etc/nginx/sites-enabled
RUN cp /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]