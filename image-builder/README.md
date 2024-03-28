Project Title
================
Packer is used to build Custom Amazon Machine Images


installation and Configuration set up 
=======================================

$sh hardening.sh

reference: https://github.com/krishnamaram2/WebApp


Execution Flow
===========================

step 1: clone repo

$git clone https://github.com/krishnamaram2/Image_Builder.git


step 2: enter src directory

$cd Image_Builder/src


step 3: enter access key and secret key

vi variables.json

{

    "aws_access_key": "",
    
    "aws_secret_key": "",
    
    "region": "us-east-1"
    
  }


Step 4: validate syntax

packer validate -var-file=variables.json builders.json


Step 5: Build custome AMI

packer build -var-file=variables.json builders.json

