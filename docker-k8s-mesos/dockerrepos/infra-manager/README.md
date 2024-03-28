Project Title
=====================
Terraform is used to provision and manage IT Infrastructure

Execution Flow
===========================

$git clone https://github.com/containerrepos/infra-manager.git


$cd  infra-manager

$vi terraform/modules/instances/instances.tf

"ami" : "CUSTOM-AMI-ID"

$ docker image build -t myinfraami .

$docker run -it -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} -e AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} myinfraami
