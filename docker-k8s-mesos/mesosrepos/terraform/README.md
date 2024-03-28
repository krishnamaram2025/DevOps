Project Title
=====================
Terraform is used to provision and manage IT Infrastructure

Pre-Requisites
============================

# Step 1: Launch ec2 instance to run terraform with name sandbox

Login to sandbox instance

$sudo yum install git -y

$git clone https://github.com/containerrepos/DevOps.git

$cd DevOps

$sh sandbox.sh

$source export.sh

# Step 2: Build Custom AMI

$git clone https://github.com/containerrepos/custom-ami.git

$cd custom-ami/packer/

$/usr/bin/packer build builders.json


Execution Flow
=====================

# source cluster

# Step 1: Bring up cluster

$git clone https://github.com/cssporg/infra_manager.git

$cd infra_manager

$vi config.json

"myregion" : ""

myamiid : ""

$terraform init .

$terraform validate -var-file=config.json

$terraform apply -var-file=config.json


# Step 2:  login to lb1 instance 
sudo yum instamm mysql -y
mysql -h mysqldb.cwxnaqnigvhg.us-east-1.rds.amazonaws.com -P 3306 -u cloud -p cloudstones


CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT INTO `student` VALUES (1,'krishna','maram','krishnamaram2@gmail.com');

# Step 3:  login to lb1 instance

login to lb1 instance 

eval `ssh-agent`

ssh-add -k .pem

ssh -A centos@publicip




sudo yum install docker -y && sudo systemctl start docker && sudo groupadd docker && sudo usermod -aG docker $USER && sudo chmod 777 /var/run/docker.sock

$git clone https://github.com/csporg/webapp.git

$cd webapp/src/haproxy

$vi haproxy.cnf(line numbers 77 and 80)

$ docker build -t my-haproxy .

$ docker run -d --name my-running-haproxy -p 80:80 my-haproxy


# Step 4 :  login to lb1 instance
login to app1 instance

sudo yum install docker -y && sudo systemctl start docker && sudo groupadd docker && sudo usermod -aG docker $USER && sudo chmod 777 /var/run/docker.sock

$git clone https://github.com/csporg/webapp.git

$cd webapp/src/flask

vi index.py

$docker image build -t flask . or $docker image build -t flask --network host .

$docker run -d --name flask -p 5001:5001 flask








# Destination cluster

$git clone https://github.com/cssporg/infra_manager.git

$cd infra_manager

$vi config.json

mykeypair : ""

myamiid : ""


$ vi modules/computing/ec2/instances.tf

variable "wrpilwsn" {

type = "list"

default = [

"10.0.20.52,0",

"10.0.20.86,1"

]

}


#subnet_id = "${var.enable_user_defined_ips ? element(var.appsubnet, element(split(":", element(var.appserver_pa_ips, count.index)),1)) : element(var.appsubnet, count.index)}"

#private_ip = "${var.enable_user_defined_ips ? element(split(":", element(var.appserver_pa_ips, count.index),0)) : ""}"

subnet_id = "${element(var.appsubnet, element(split(",", element(var.wrpilwsn, count.index)), 1))}"

private_ip = "${element(split(",", element(var.wrpilwsn, count.index)), 0)}"


$terraform init .

$terraform validate -var-file=config.json

$terraform apply -var-file=config.json



# After disaster

vi config.json

"rds_mysql_db" : {
  "recover" : "true",
  "snapshot_names" : "rds-mysql-db-snp"
}

