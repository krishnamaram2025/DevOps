#!/usr/bin/env python
import os

cmds = ["sudo git clone https://github.com/krishnamaram2/configuration-manager.git && cd ./configuration-manager/src", "sudo ansible-palybook -i  ./configuration-manager/src/webapp/hosts  ./configuration-manager/src/webapp/plays/webapp.yml"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
