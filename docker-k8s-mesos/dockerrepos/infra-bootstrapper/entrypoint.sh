#!/bin/sh
mkdir -p /etc/ansible
echo "localhost" > /etc/ansible/hosts

mkdir -p /centos/.ssh
ssh-keygen -f /centos/.ssh/id_rsa -P ""

cp /hostssh/authorized_keys /hostssh/authorized_keys.orig
cat /centos/.ssh/id_rsa.pub >> /hostssh/authorized_keys
ansible-playbook plays/cicd.yml
mv /hostssh/authorized_keys.orig /hostssh/authorized_keys
