# package-manager
Helm is used to install and manage packages


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

helmfile destroy


Reference: 

https://github.com/thedataincubator/flask-chart

https://github.com/helm/charts/tree/master/stable/mysql

https://lyz-code.github.io/blue-book/devops/helmfile/

https://medium.com/@mattiaperi/create-a-public-helm-chart-repository-with-github-pages-49b180dbb417

https://medium.com/swlh/how-to-declaratively-run-helm-charts-using-helmfile-ac78572e6088

https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/

https://wkrzywiec.medium.com/how-to-deploy-application-on-kubernetes-with-helm-39f545ad33b8a

