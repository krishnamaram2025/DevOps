############################################################################################
#####                     Creating  Docker Image using Multi-stage builds             ######
############################################################################################

#Stage1
#Pull the  Base Image from the Docker default registry i.e Docker Hub
FROM python:3 as base 
#AUTHOR
LABEL "AUTHOR"="krishnamaram2@gmail.com"
# Create the user with name macuser and with home directory as /home/macuser
RUN useradd -m macuser 
USER macuser
#Configuring working directory 
WORKDIR /home/macuser 

#Stage2
FROM base 
#Copying the python program to working directory 
COPY ./macaddress.py /home/macuser
#Execute the program  
ENTRYPOINT ["python3", "macaddress.py"]
