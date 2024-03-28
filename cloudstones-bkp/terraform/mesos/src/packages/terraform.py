#!/usr/bin/env python3

import subprocess

cmds = ["terraform  init providers/aws/ && terraform validate -var-file=clusters/aws/dev.json providers/aws && terraform apply -var-file=clusters/aws/dev.json -auto-approve providers/aws"]

for cmd in cmds:
    print("command name", cmd)
    cmd_execution = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)
    cmd_output, cmd_error = cmd_execution.communicate()
    print("output of the command", cmd_output)

