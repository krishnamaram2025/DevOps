
$git clone https://github.com/containerrepos/infra-bootstrapper.git

$cd infra-bootstrapper

$ansible-playbook plays/webserver.yml

$docker image build -t mywebserver .

$docker container run -it --net=host -v /root/.ssh:/hostssh mywebserver
