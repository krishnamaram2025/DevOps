# Project Title
This project is intended to touch and feel containerized Web Application. 

# Pre-Requisites

Launch ec2 instance to run terraform with name sandbox

Login to sandbox instance

$sudo yum install git -y 

$git clone https://github.com/containerrepos/DevOps.git

$cd DevOps

$sh sandbox.sh

$source export.sh

# Step 1: Build Base AMI
https://github.com/containerrepos/base-ami

# Step 2: Build Custom AMI with Packer
https://github.com/containerrepos/custom-ami.git

# Step 3: Provisioning infrastructure with Terraform
https://github.com/containerrepos/infra-manager

# Step 4: Installing and configuring Web server using Ansible
https://github.com/containerrepos/infra-bootstrapper

# Step 5: Result
http://PUBLICIP:80
