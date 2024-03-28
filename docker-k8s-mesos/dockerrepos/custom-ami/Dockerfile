FROM alpine:3.13

MAINTAINER Krishna Maram

# apk has ansible 1.9 but not 2.x 
RUN apk update && apk upgrade && apk add --no-cache  python3 py-pip python3-dev libffi-dev build-base openssl openssl-dev gcc musl-dev openssh curl linux-headers jq \
    && pip install --upgrade pip \
    && pip install "ansible~=2.8.2" \
    && pip install awscli

ADD https://releases.hashicorp.com/packer/1.5.5/packer_1.5.5_linux_amd64.zip /
ADD https://releases.hashicorp.com/terraform/0.14.10/terraform_0.14.10_linux_amd64.zip /
RUN unzip packer_1.5.5_linux_amd64.zip -d /usr/bin/ \
   && unzip terraform_0.14.10_linux_amd64.zip -d /usr/bin \ 
   && rm /packer_1.5.5_linux_amd64.zip \
   && rm /terraform_0.14.10_linux_amd64.zip \
   && apk del build-base
    
ADD entrypoint.sh /entrypoint.sh
ADD packer /packer
RUN chmod -R 755 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
