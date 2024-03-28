$git clone https://github.com/devopsstackorg/middleware.git

$cd middleware

$docker image build -t app-i .

$docker container run -d -it --name app-c -p 8080:8080 app-i

$git clone https://github.com/krishnamaram2/WebApp.git

$docker cp WebApp/binaries/Student.war <container_id>:/usr/local/tomcat/webapps/

$docker exec -it <container_name> sh

$vi webapps/Student/WEB-INF/classes/application.properties

