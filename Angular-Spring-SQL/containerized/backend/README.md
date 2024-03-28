$git clone https://github.com/devopsstackorg/backend.git

$cd backend

$docker image build -t db-i .

$docker run -it -d --name db-c -e MYSQL_ROOT_PASSWORD=Root_123 db-i

$docker exec -it db-c sh

Step 3: create database and user for MySQL and import data into database $docker exec -it <container_name> sh

$mysql -u root -p

mysql>create database indigo;

mysql>CREATE USER 'krishna'@'%' IDENTIFIED BY 'Krishna_123';

mysql>GRANT ALL ON *.* TO 'krishna'@'%';

mysql>FLUSH PRIVILEGES;

$git clone https://github.com/krishnamaram2/WebApp.git

$cd WebApp/binaries

$mysql -u <user_name> -p indigo < indigo.sql
