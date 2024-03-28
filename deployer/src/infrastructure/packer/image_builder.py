#!/usr/bin/env python
import os

cmds = ["sudo git clone https://github.com/krishnamaram2/image-builder.git && cd ./image-builder/src", "packer validate -var-file=./image-builder/src/variables.json ./image-builder/src/builders.json && packer build -var-file=./image-builder/src/variables.json ./image-builder/src/builders.json"]

for cmd in cmds:
    print("commnad to execute", cmd)
    os.system(cmd)
    
