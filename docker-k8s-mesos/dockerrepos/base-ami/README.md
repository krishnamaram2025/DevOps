Project Title
================
Packer is used to build Custom Amazon Machine Images

Execution Flow
===========================
yum install epel-release -y

yum install ansible -y

step 1: clone repo

$git clonehttps://github.com/containerrepos/base-ami.git

$cd base-ami

$docker image build -t mybaseami .

$docker run -it -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e  AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}  -e AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} mybaseami

