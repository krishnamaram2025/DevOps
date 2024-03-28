# Project Title
This project is intended to touch and feel containerized Web Application. 

# Step 1: Bring up destination cluster

$git clone https://github.com/cssporg/terraform.git

# Step 2: Changes in config.json

$cd terraform

$vi config.json

mykeypair : ""

"myregion" : ""

myamiid : ""

"rds_mysql_db" : {
  "recover" : "true",
  "snapshot_names" : "rds-mysql-db-snp"
}

# Step 3: Changes in modules/computing/ec2/instances.tf file

$ vi modules/computing/ec2/instances.tf

variable "wrpilwsn" {

type = "list"

default = [

"10.0.20.52,0",

"10.0.20.86,1"

]

}

subnet_id = "${element(var.appsubnet, element(split(",", element(var.wrpilwsn, count.index)), 1))}"

private_ip = "${element(split(",", element(var.wrpilwsn, count.index)), 0)}"

# Step 4: Execute terraform apply

$terraform init .

$terraform validate -var-file=config.json

$terraform apply -var-file=config.json

# Step 5: take public ip of lb1 instance and app1 instance and run ansible playbook
sudo systemctl start docker && sudo groupadd docker && sudo usermod -aG docker $USER && sudo chmod 777 /var/run/docker.sock
$sh /etc/csp/boot_scripts/play-books.sh

OR

http://PUBLICIP:80
