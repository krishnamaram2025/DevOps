
#ssh-keygen -q -t rsa -N '' -f /home/centos/.ssh/id_rsa <<<y 2>&1 >/dev/null
#cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys
#ssh -o StrictHostKeyChecking=no centos@localhost
