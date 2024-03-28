#!/usr/bin/env python
import os

cmds = ["sudo ssh-keygen -q -t rsa -N '' -f /home/centos/.ssh/id_rsa <<<y 2>&1 >/dev/null",
"sudo cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys",
"sudo ssh -o StrictHostKeyChecking=no centos@localhost"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
