#!/usr/bin/env python
import os

cmds = ["sudo git clone https://github.com/krishnamaram2/infrastructure-manager.git && cd ./infrastructure-manager/src/webapp", "sudo terraform init ./infrastructure-manager/src/webapp/ && sudo terraform  validate ./infrastructure-manager/src/webapp  && sudo terraform apply -auto-approve  ./infrastructure-manager/src/webapp"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
