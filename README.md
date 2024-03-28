# DevOps    =  Dev  +  Ops   =   Development + Operations
This project is implemented to touch and feel the DevOps Pipeline

# Pre-Requisites
IAM User Access Keys

Region

KeyPair

AMI ID

# Phase 0: launch ec2 instance and named as "Sandbox"

Step 1: Launch EC2 instance from the AWS Console and logging into EC2 instance and install git tool

$sudo yum install git -y

Step 2: clone deployer git repo

$sudo git clone https://github.com/krishnamaram2025/DevOps.git

Step 3: Install all the necessary packages  

$python ~/deployer/src/sandbox/sandbox.py


# Phase 1: Build custom AMI using "Packer"

$python ./deployer/src/infrastructure/packer/image_builder.py


# Phase 2: Provision infrastructure using "Terraform"

$python ./deployer/src/infrastructure/terraform/infrastructure_manager.py


# Phase 3: Configure Softwares using "Ansible" 

$python ./deployer/src/infrastructure/ansible/ssh_keys.py

$python ./deployer/src/infrastrcuture/ansible/play_books.py
