#!/bin/sh -eux

#install EPEL repository
sudo yum -y install epel-release

#Install Ansible
sudo yum -y install ansible python-setuptools
