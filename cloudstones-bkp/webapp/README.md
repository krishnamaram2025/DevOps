Title
=================
This project is implemented to touch and feel Python Falsk WebApp

# Technologies
Python

Flask 

MySQL
                                                             
                                                             
                                               Traditional Web App
                                                           
Middle ware Python Flask
-----------------------------------
$sudo yum update -y && sudo yum install epel-release -y && sudo yum install wget -y && sudo yum install git -y 

$sudo yum install python-pip -y

$sudo yum install mysql mysql-devel mysql-common mysql-libs gcc  python3-devel -y

$sudo pip3 install Flask

$sudo pip3 install mysqlclient==1.3.1

$sudo pip3 install Flask-MySQLdb

$sudo pip3 install gunicorn

$git clone https://github.com/csporg/webapp.git

$cd ./webapp/src/flask

$gunicorn --bind 0.0.0.0:5001 wsgi
 
http://<public_ip>:5001/
 
Reeference: 
 
https://pybuilder.io/documentation/tutorial
 
https://github.com/pyclectic/flask-example

Backend  MySQL 
------------------------
$wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm

$md5sum mysql57-community-release-el7-9.noarch.rpm

$sudo rpm -ivh mysql57-community-release-el7-9.noarch.rpm

$sudo yum install mysql-server -y

$sudo systemctl start mysqld

$sudo systemctl status mysqld

$sudo grep 'temporary password' /var/log/mysqld.log

$sudo mysql_secure_installation

$mysqladmin -u root -p version

Step 3:create database and user for MySQL

$mysql -u root -p

mysql>create database cloudstones;

mysql>CREATE USER 'cloud'@'%' IDENTIFIED BY 'Cloud_123';

or

CREATE USER 'cloud'@'%' IDENTIFIED WITH mysql_native_password BY 'Cloud_123';

mysql>GRANT ALL ON *.* TO 'cloud'@'%';

mysql>FLUSH PRIVILEGES;

$git clone https://github.com/csporg/webapp.git

$mysql -u cloud -p cloudstones < webapp/src/mysql/cloudstones.sql




                                               Distributed Web App


Python Flask
--------------
$git clone https://github.com/csporg/webapp.git

$cd webapp/src/flask

$docker image build -t flask .   or      $docker image build -t flask --network host  .

$docker run -d --name flask -p 5001:5001 flask

https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-centos-7


MySQL
----------
$git clone https://github.com/csporg/webapp.git

$cd webapp/src/mysql

$docker image build -t mysql .

$docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Root_123 mysql

https://medium.com/better-programming/customize-your-mysql-database-in-docker-723ffd59d8fb


# Registry

$docker image tag flask csporg/flask:master_1

$docker image push csporg/flask:master_1

$docker login

$docker pull csporg/flask:master_1

$docker run -d --name flask -p 5001:5001 csporg/flask:master_1


# Registry

$docker image tag mysql csporg/mysql:master_1

$docker image push csporg/mysql:master_1

$docker login

$docker pull csporg/mysql:master_1

$docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Root_123 csporg/mysql:master_1


