# Step 1: create AMI using Packer
https://github.com/devops2023q2/packer

# Step 2: Create infrastructure and WebApp server using Terraform
https://github.com/devops2023q2/terraform

# Step 3: Install and configure software packages using Ansible
https://github.com/devops2023q2/ansible

# Step 4: Deploy WebApp in gunicorn server
* Fix temp bug: (line 67 replace > with ==)
```
sudo vi /usr/local/lib64/python3.6/site-packages/django/db/backends/sqlite3/base.py 
```
* Python automation to deploy webapp
* 
https://github.com/devops2023q2/deployer

# Step 5: Assign public ip to Domain in GoDaddy
