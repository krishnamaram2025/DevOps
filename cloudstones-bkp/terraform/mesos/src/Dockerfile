FROM alpine:3.13

MAINTAINER Krishna Maram

ENV TERRAFORM_VERSION=0.14.6

ENV CSP_CMD "--help"

RUN apk update && \
    apk add curl jq python3 python3-dev bash ca-certificates git openssl unzip wget && \
    cd /tmp && \
    wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/* && \
    rm -rf /var/tmp/*
    
ADD . /mesos-terraform

WORKDIR /mesos-terraform

ENTRYPOINT ./entrypoint.py ${CSP_CMD}
