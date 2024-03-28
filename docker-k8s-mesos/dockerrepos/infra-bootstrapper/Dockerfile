FROM alpine:3.13

MAINTAINER Krishna Maram

RUN apk add --no-cache  py-pip python3-dev libffi-dev build-base gcc openssl-dev musl-dev openssh \ 
    && pip install --upgrade pip \
#    && pip install --upgrade boto six \
    && pip install --upgrade ansible~=2.8.2 \
    && pip install paramiko \
    && rm -rf /var/cache/apk \
    && apk del build-base 

ENV ANSIBLE_CONFIG=/ansible.cfg
ADD entrypoint.sh /entrypoint.sh
ADD ansible.cfg /ansible.cfg    
ADD plays /plays
ADD roles /roles
RUN chmod 755 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

