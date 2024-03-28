# DevOps
This project is intended to touch and feel DevOps methodology.

# Technologies used
Developement: HTML,Python, DJango, SQL, SQLITE, Gunicorn, VS code, Draw.io

Operations: AWS(VPC, EC2, EBS)

DevOps: GitHub, Git, Packer, Terraform, Ansible

To be implemented: Jenkins, Artifactory

# Development Team: Run DJango App locally 
Step 1: Download webapp.zip and Extract to local machine folder Downloads and enter into webapp folder
```
cd webapp
```
Step 2: Run migration to create table in SQLite database
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Step 3: Run DJangi inbuild developement server
```
python manage.py runserver
```
Step 4: Test the app from the browser
```
http://127.0.0.1:8000
```

# Architecture Diagrams
![image](https://user-images.githubusercontent.com/112494492/235676293-0fe26b47-b197-4a27-aec0-9703cab619ad.png)
![image](https://user-images.githubusercontent.com/112494492/235676429-ab61a488-2f7a-4829-8b14-c3817aaae048.png)

# Operations Team: Provision Infrastructure and Application deployment using Traditional approach
https://github.com/devops2023q2/DevOps/blob/master/ManualSetUp.md

# DevOps Team: Provision Infrastructure and Application deployment using DevOps approach
https://github.com/devops2023q2/DevOps/blob/master/AutomateSetUp.md
