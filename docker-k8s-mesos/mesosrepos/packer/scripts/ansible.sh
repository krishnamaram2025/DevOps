#!/bin/sh -eux

#install EPEL repository
sudo yum -y install epel-release 

#Install Ansible
sudo yum -y install ansible python-setuptools

#sudo yum install ansible -y
sudo yum install docker -y
sudo systemctl start docker
sudo groupadd docker
sudo usermod -aG docker $USER
sudo chmod 777 /var/run/docker.sock
