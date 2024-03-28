#Shebang
#!/usr/bin/env python

# importing statements
import subprocess

# Linux commands to execute
#yum update -y && yum upgrade -y && yum install epel-release -y
cmds = ["sudo yum install git -y && sudo yum install wget -y && sudo yum install curl -y && sudo yum install unzip -y",
"sudo wget https://releases.hashicorp.com/packer/1.5.5/packer_1.5.5_linux_amd64.zip && sudo unzip packer_1.5.5_linux_amd64.zip && sudo mv packer /bin/ && sudo rm -rf ./packer*",
"sudo wget https://releases.hashicorp.com/terraform/0.14.10/terraform_0.14.10_linux_amd64.zip && sudo unzip terraform_0.14.10_linux_amd64.zip && sudo mv terraform /bin/ && sudo rm -rf ./terraform*",
"sudo cp ~/deployer/src/sandbox/ansible.repo /etc/yum.repos.d/ && sudo yum install ansible -y",
"sudo curl 'https://s3.amazonaws.com/aws-cli/awscli-bundle.zip' -o 'awscli-bundle.zip' && sudo unzip awscli-bundle.zip && sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && sudo rm -rf ./awscli-bundle*"]
#yum update -y && yum upgrade -y && yum install epel-release -y

#Logic to execute all the commands one by one
for cmd in cmds:
    print("command name", cmd)
    cmd_execution = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)
    cmd_output, cmd_error = cmd_execution.communicate()
    print("output of the command", cmd_output)



#!/usr/bin/env python
import os
cmd = "aws configure"
os.system(cmd)    
