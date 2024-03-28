FROM centos:7
MAINTAINER "krishnamaram2@gmail.com"
LABEL purpose="this Dockerfile is used to build apache web server"
RUN yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install httpd && \
    yum clean all
#RUN  yum install git -y
#EXPOSE 80
# Simple startup script to avoid some issues observed with container restart
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh
CMD ["/run-httpd.sh"]
