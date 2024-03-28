##########################################################################################
#####               Wrapper script to run Containerized application                  #####
##########################################################################################
#!/bin/bash
arg=``
count=0
case $@ in
$arg)
     echo -e "\n"
     read -p "Please Enter  Your API Key: "  API_KEY
     echo -e "\n"
     if [ ! -f macaddress.txt ] ||  [ -z "$(cat macaddress.txt)" ]; then
       read -p "Please Enter your MAC Address: "  MAC_ADDRESS
       echo -e "\n \n \n"
       echo -e "Docker Image creation and running the container is under progress...\n"
       #Build the Image using  Dockerfile
       docker image  build -t mac_addr . > /dev/null 2>&1
       #Run the container and pass API_KEY and MAC_ADDRESS as arguments
       docker container run  mac_addr $API_KEY $MAC_ADDRESS
       echo -e "\n \n \n"
     else
         echo -e "Docker Image creation and running the container is under progress...\n"
         for MAC_ADDRESS in `cat macaddress.txt`;
           do
            count=$((count+1))
           if [ $count == 1 ]; then
              #Build the Image using  Dockerfile
              docker image build -t mac_addr . > /dev/null 2>&1
              #Run the container and pass API_KEY and MAC_ADDRESS as arguments
              docker container run -it mac_addr $API_KEY $MAC_ADDRESS
           else
              #Run the container and pass API_KEY and MAC_ADDRESS as arguments
              docker container run -it mac_addr $API_KEY $MAC_ADDRESS
              echo -e "\n \n \n"
             fi
            done
     fi
   ;;
*)
    echo "$(cat README.md)"
;;
esac
