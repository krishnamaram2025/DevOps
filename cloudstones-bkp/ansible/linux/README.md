Project Title
========================
Ansible is used for Software configuration purpose



 #!/bin/bash
 
 ssh-keygen -q -t rsa -N '' -f /home/centos/.ssh/id_rsa <<<y 2>&1 >/dev/null

 cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys

 ssh -o StrictHostKeyChecking=no centos@localhost


Execution Flow
======================

step 1: clone repo

$git clone https://github.com/cloudstones/linux-ansible.git

Step 2: run playbooks

$cd linux-ansible/src/

$ansible-playbook -i hosts plays/opsstack.yml



