
# CICD Cluster
# Step 1: Provision infrastructure in AWS
=>Networking 
```
-> Launch VPC with name myvpc with cidr : 10.0.0.0/16 
   
-> Launch Internet Gateway named as myigw 
   
-> Launch Subnet with name mysubnet with cidr 10.0.1.0/24 
   
-> Launch Route Table with myrtb 
   
-> Follow the below steps to configure internet connection.(otherwise we can’t connect to resources which resides in myvpc from our local network) 

attach myigw to myvpc

add myigw to routes in myrtb(destination 0.0.0.0/0, target myigw)

associate mysubnet in myrtb 
```
=>Security
```
->Security group with name mysg(add inbound rule to open traffic for all ports)

-> Create keypair with name mykp(select private key file format as a .pem)
```
=>Computing
```
-> Launch 2 EC2 instances(centos7 image) with name jenkins-server and artifactory-server
    Note: Auto-assign public IP : Enable
```
        
# Stpe 2: Install and configure required software packages for Jenkins
* Login to Jenkins sever
```
ssh -i <<mykp>> centos@<<PUBLIC_IP>>
sudo yum install wget -y
sudo yum install java-11-openjdk-devel -y
curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key 
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo 
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key 
sudo yum install jenkins -y
sudo systemctl start jenkins 
sudo systemctl enable jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword
http://<<PUBLIC_IP>>:8080/
click on Install suggested plugins
```

* Login to Artifactory sever
```
ssh -i <<mykp>> centos@<<PUBLIC_IP>>
sudo yum install -y net-tools rsync wget
sudo yum install -y java-1.8.0-openjdk-devel 
sudo su 
echo "export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.191.b12-1.el7_6.x86_64" >> /etc/profile 
source /etc/profile 
env | grep JAVA
sudo wget https://releases.jfrog.io/artifactory/artifactory-rpms/artifactory-rpms.repo -O jfrog-artifactory-rpms.repo 
sudo mv jfrog-artifactory-rpms.repo /etc/yum.repos.d/ 
sudo yum update -y && sudo yum install jfrog-artifactory-oss -y 
sudo echo "export ARTIFACTORY_HOME=/opt/jfrog/artifactory" >> /etc/profile 
source /etc/profile 
env | grep ARTIFACTORY_HOME
sudo systemctl start artifactory.service 
systemctl enable artifactory.service 
http://<<PUBLIC_IP>>:8081
```
# WebApp cluster
# Step 1: Provision infrastructure in AWS
=>Networking 
```
-> Launch VPC with name myvpc with cidr : 10.0.0.0/16 

-> Launch Internet Gateway named as myigw 

-> Launch Subnet with name mysubnet with cidr 10.0.1.0/24 

-> Launch Route Table with myrtb 

-> Follow the below steps to configure internet connection.(otherwise we can’t connect to resources which resides in myvpc from our local network) 

->attach myigw to myvpc

->add myigw to routes in myrtb(destination 0.0.0.0/0, target myigw)

->associate mysubnet in myrtb 
```

=>Security
```
-> Security group with name mysg(add inbound rule to open traffic for all ports)

->  Create keypair with name mykp(select private key file format as a .pem)
```

=>Computing
```
-> Launch 2 EC2 instance(centos7 image) with name gunicorn server and HAProxy server
    Note: Auto-assign public IP : Enable
```
 
* Login to gunicorn sever
```
ssh -i <<mykp>> centos@<<PUBLIC_IP>>
sudo yum install git -y
sudo yum install python3-pip -y
sudo pip3 install django
sudo vi /usr/local/lib64/python3.6/site-packages/django/db/backends/sqlite3/base.py  (line 67   replace > with ==)
sudo pip3 install gunicorn
gunicorn main.wsgi --bind 0.0.0.0:8000
http://PUBLIC_IP:8000
```
* Login to HAProxy sever
```
sudo yum install haproxy -y
git clone https://github.com/csporg/webapp.git
cd webapp/src/haproxy/haproxy.cfg
cp /etc/haproxy 
sudo haproxy -f /etc/haproxy/haproxy.cfg -c
sudo systemctl restart haproxy
```
