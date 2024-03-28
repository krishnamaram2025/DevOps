# package-manager
Helm is used to install and manage packages


# Pre-Requisites
Install HELM

$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3

$ chmod 700 get_helm.sh

$ ./get_helm.sh


Install Helmfile

wget https://github.com/roboll/helmfile/releases/download/v0.142.0/helmfile_linux_386
 
sudo  mv helmfile_linux_386 helmfile
 
sudo chmod 755 helmfile && sudo  mv helmfile /usr/bin



# Execution Flow

$git clone https://github.com/cloudstones/k8s-helm.git


Deploying kubernetes manifest files using helm charts

$cd k8s-helm/src/flask-mysql-charts/flask

$helm install myflask ./

$cd k8s-helm/src/flask-mysql-charts/mysql

$helm install mymysql ./


How to deploy helm charts using helmfile

cd k8s-helm/src

helmfile sync

abeb4c01b38d842e38ff7b5b5911c6ca-1983148523.us-east-1.elb.amazonaws.com:5001(ELB endpoint)

Issues
-------
if elb not able to launch then add the below to Public subnets as TAg

kubernetes.io/cluster/<EKSClusterName> : shared

 https://stackoverflow.com/questions/62468996/eks-could-not-find-any-suitable-subnets-for-creating-the-elb

helmfile destroy


Reference: 

https://github.com/thedataincubator/flask-chart

https://github.com/helm/charts/tree/master/stable/mysql

https://lyz-code.github.io/blue-book/devops/helmfile/

https://medium.com/@mattiaperi/create-a-public-helm-chart-repository-with-github-pages-49b180dbb417

https://medium.com/swlh/how-to-declaratively-run-helm-charts-using-helmfile-ac78572e6088

https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/

https://wkrzywiec.medium.com/how-to-deploy-application-on-kubernetes-with-helm-39f545ad33b8a

