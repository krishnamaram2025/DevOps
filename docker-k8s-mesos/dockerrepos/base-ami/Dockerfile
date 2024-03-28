FROM centos:7

RUN  yum install git -y &&  yum install wget -y &&  yum install unzip -y

RUN  wget https://releases.hashicorp.com/packer/1.5.5/packer_1.5.5_linux_amd64.zip &&  unzip packer_1.5.5_linux_amd64.zip &&  mv packer /bin/ &&  rm -rf ./packer*

RUN yum install epel-release -y && yum install ansible -y

COPY packer /packer
COPY entrypoint.sh /
RUN chmod -R 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


