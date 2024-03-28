Project Title
========================
Ansible is used for Software configuration purpose


 Pre-Requisites
===============================
Case 1: manual 

step 1: switch to root user

$passwd centos

Step 2: enable password authentication

$vi /etc/ssh/sshd_config

   PasswordAuthentication yes

optional :   permitroorlogin yes

$systemctl restart sshd

step 3: generate ssh keys for password based authentication and ad ssh keys

$ssh-keygen

$ssh-copy-id centos@localhost


Case 2: automation

 #!/bin/bash
 
 ssh-keygen -q -t rsa -N '' -f /home/centos/.ssh/id_rsa <<<y 2>&1 >/dev/null

 cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys

 ssh -o StrictHostKeyChecking=no centos@localhost


Execution Flow
======================

step 1: clone repo

$git clone https://github.com/krishnamaram2/configuration-manager.git

Step 2: run playbooks

$cd configuration-manager/src/webapp

$ansible-playbook -i hosts plays/webapp.yml

$cd configuration-manager/src/devstack

$ansible-playbook -i hosts plays/devstack.yml

$cd configuration-manager/src/opsstack

$ansible-playbook -i hosts plays/opsstack.yml



