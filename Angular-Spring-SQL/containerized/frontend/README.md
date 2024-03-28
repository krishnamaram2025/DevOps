$git clone https://github.com/devopsstackorg/frontend.git

$cd frontend

$docker image build -t <image_name> .

$docker container run -it -d --name <container_name> -p 80:80 <image_name>

$docker exec -it <container_name> sh

sudo vi /var/www/html/main.js (Replace App Server IP with localhost in two lines i.e 314 and 701)
