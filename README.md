# Vagrant-Docker-MySQL-Flask
This project is about creating a VM with vagrant management. 
The following actions will be performed on the vagrant VM with the help of ansible playbook (which runs automatically at VM start):
- installs Ubuntu prereq packages
- installs MySQL service
- it clones the git repo https://github.com/datacharmer/test_db and imports employees_partitioned.sql DB
- installs Docker service and its dependencies
- clones this repo and builds docker image from Dockerfile, named querydb
- starts docker container, named pythonapp

Vagrantfile
-----------
- maps the port 80 to 1234 on the host
- installs python 2.7

Dockerfile
----------
- nginx
- flask
- app.py

app.py
------
- queries the employees database from MySQL VM
- displays the results in html format

How to run it:
--------------

> vagrant up

Wait until ansible provisioning ends. Open a browser and type in: http://localhost:1234, it should display the results in html format.
