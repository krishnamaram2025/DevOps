# DevOps    =  Dev  +  Ops   =   Development + Operations
 
This project is implemented to touch and feel the DevOps Pipeline

$git clone https://github.com/cloudstones/linux-DevOps.git

docker image build -t kri .

docker container run -it -d -p 8080 kri

http://PUBLIC_IP:8080/Student

kubectl create -f webapp.yaml

http://LOAD_BALANCER:8080/Student

# Set up Sandbox, Maven, Jenkins, Artifactory, Tomcat, Docker, k8s servers

# Set up Single node Kubernetes cluster

sudo yum install yum-utils -y && sudo yum install device-mapper-persistent-data -y && sudo yum install lvm2 -y

sudo wget  https://download.docker.com/linux/centos/docker-ce.repo 

sudo cp docker-ce.repo /etc/yum.repos.d/docer-ce.repo

sudo yum install containerd.io-1.2.13 -y && sudo yum install docker-ce-19.03.11 -y && sudo yum install docker-ce-cli-19.03.11 -y

sudo mkdir /etc/docker

sudo mkdir /etc/systemd/system/docker.service.d

sudo systemctl daemon-reload

sudo systemctl restart docker

sudo vi /etc/yum.repos.d/kubernetes.repo

[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
#exclude=kubelet kubeadm kubectl


sudo yum install kubeadm -y && sudo yum install kubectl -y && sudo yum install kebelet -y

sudo systemctl restart kubelet

sudo echo 1 >  /proc/sys/net/bridge/bridge-nf-call-iptables

sudo kubeadm init

sudo mkdir $HOME/.kube

sudo chmod 0755 $HOME/.kube

sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown centos:centos $HOME/.kube/config

sudo chmod 0755 $HOME/.kube/config

kubectl apply -f  /home/centos/configuration-manager/src/opsstack/weavenet.yml

kubectl taint nodes --all node-role.kubernetes.io/master-

kubectl create -f webapp.yaml


# Pre-Requisites
IAM User Access Keys

Region : us -east-1

KeyPair - virginia

AMI ID : (for example ami-0affd4508a5d2481b)



# Phase 0: launch ec2 instance and named as "Sandbox"

Step 1: Launch EC2 instance from the AWS Console and logging into EC2 instance and install git tool

$sudo yum install git -y

Step 2: clone deployer git repo

$sudo git clone https://github.com/krishnamaram2/deployer.git

Step 3: Install all the necessary packages  

$python ~/deployer/src/sandbox/sandbox.py


# Phase 1: Build custom AMI using "Packer"

$git clone https://github.com/cloudstones/linux-packer.git

$cd linux-packer/src

$packer validate -var-file=variables.json builders.json

$packer build -var-file=variables.json builders.json


# Phase 2: Provision infrastructure using "Terraform"

$python ./deployer/src/infrastructure/terraform/infrastructure_manager.py


# Phase 3: Configure Softwares using "Ansible" 

#!/bin/bash

ssh-keygen -q -t rsa -N '' -f /home/centos/.ssh/id_rsa <<<y 2>&1 >/dev/null

cat /home/centos/.ssh/id_rsa.pub >> /home/centos/.ssh/authorized_keys

ssh -o StrictHostKeyChecking=no centos@localhost

step 1: clone repo

$git clone https://github.com/cloudstones/linux-ansible.git

Step 2: run playbooks

$cd linux-ansible/src/

$ansible-playbook -i hosts plays/opsstack.yml
