Project Title
================
Packer is used to build Custom Amazon Machine Images

Execution Flow
===========================

$git clone https://github.com/containerrepos/custom-ami.git


step 2: enter src directory

vi custom-ami/packer/builders.json

"source_ami": "BASEAMI-ID",

$cd custom-ami


$ docker image build -t mycustomami .

$docker run -it -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} -e AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} mycustomami
