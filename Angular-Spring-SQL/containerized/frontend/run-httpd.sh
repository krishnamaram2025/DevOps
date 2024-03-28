#!/bin/bash

# Make sure we're not confused by old, incompletely-shutdown httpd
# context after restarting the container.  httpd won't start correctly
# if it thinks it is already running.
rm -rf /run/httpd/* /tmp/httpd*
yum install git -y
git clone https://github.com/krishnamaram2/WebApp.git
cp -rf ./WebApp/binaries/dist/* /var/www/html/
exec /usr/sbin/apachectl -DFOREGROUND
