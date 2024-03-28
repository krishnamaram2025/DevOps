sudo yum install epel-release -y
sudo yum install git -y && sudo yum install wget -y && sudo yum install unzip -y
sudo wget https://releases.hashicorp.com/packer/1.5.5/packer_1.5.5_linux_amd64.zip && sudo unzip packer_1.5.5_linux_amd64.zip && sudo mv packer /bin/ && sudo rm -rf ./packer*
sudo wget https://releases.hashicorp.com/terraform/0.14.10/terraform_0.14.10_linux_amd64.zip && sudo unzip terraform_0.14.10_linux_amd64.zip && sudo mv terraform /bin/ && sudo rm -rf ./terraform*
sudo yum install ansible -y
sudo yum install docker -y
sudo systemctl start docker
sudo groupadd docker
sudo usermod -aG docker $USER
sudo chmod 777 /var/run/docker.sock
