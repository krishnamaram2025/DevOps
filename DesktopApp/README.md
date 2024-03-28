Project Title
=====================

Application for fetching  the Company Name associated with respective MAC address using the API.


Technologies 
=====================
Programming Language: Python

Scripting language: Bash scripting

Container Engine: Docker


Pre-Requisites
======================
1.Generate API Key(https://macaddress.io/)

2.Linux Operating System

3.Install Docker

4.Install python3(Optional)



Implementation Process
======================

The below steps are optional, may be used to test at various stages like application development, image baking process etc

Step 1: Implemeted Python program to fetch Data like Company Name and Country code for respective MAC Address

                           $python3 macaddress.py <API_KEY> <MAC_ADDRESS>
                          
Step 2: Containerized Application using multi-stage builds to improve Maintainability and readability

                           $docker build -t <Tag-Name>  .
                           $docker container run -it <Image-Id>/<Tag-Name> <API_KEY> <MAC_ADDRESS>
                           
                           
Execution Flow
====================


Implemented wrapper script named macaddress.sh, invoking the same would fetch the required information of the MAC Addresses

 case1: In order to obtained the Company Name of required MAC Addresses, store all the MAC Addresses in the file named macaddress.txt  and run the below command  
 
                           $bash macaddress.sh
                           Please Enter  Your API Key: <API_KEY>
 case2: If the macaddress.txt file not exist or file is empty, then it will prompt you  to enter the API Key and MAC Address
 
                           $bash macaddress.sh
                           Please Enter  Your API Key: <API_KEY>
                           Please Enter your MAC Address: <MAC_ADDRESS>
                           
   The output looks like :
 
MAC Address        :    44:38:39:ff:ef:57

Company Name       :    Cumulus Networks, Inc

Company Address    :    650 Castro Street, suite 120-245 Mountain View  CA  94041 US

Country code       :    US
