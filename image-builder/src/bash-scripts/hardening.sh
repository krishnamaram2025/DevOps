#sudo yum update -y
#sudo yum upgrade -y
#sudo yum install git -y
#sudo yum install wget -y
#sudo yum install curl -y
#sudo yum install unzip -y
sudo cp /home/centos/ansible.repo /etc/yum.repos.d/
#sudo cp /home/centos/docker-ce.repo /etc/yum.repos.d/
sudo yum install ansible -y
sudo yum install docker -y

