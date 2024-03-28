#FROM dockerbase/tomcat8
#ADD run-tomcat.sh /run-tomcat.sh
#RUN chmod -v +x /run-tomcat.sh
#ENTRYPOINT ["/run-tomcat.sh"]
FROM tomcat:9.0-alpine
LABEL maintainer="deepak@softwareyoga.com"
#RUN apk add openjdk8=8.242.08-r0
RUN apk add openjdk8-jre
#ADD Student-1.0.war /usr/local/tomcat/webapps/

EXPOSE 8080
CMD ["catalina.sh", "run"]

