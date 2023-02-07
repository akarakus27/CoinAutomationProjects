# Paribu Test Automation

Paribu is test automation written in python selenium
## Requirements
* Python 3
* Selenium
* Chrome
* PyCharm IDE
* Selenium Grid
## Tests 
* Coinler listele ve  bir excel dosyasınna coin iismi-fiyat-değişim oranı şeklinde
yazdır
* Login test 
* Footer seciton test

### Test case
https://docs.google.com/spreadsheets/d/19UN7GEZ7650zbr8MqTulkqAVydh5MzvTHsKXszNwO94/edit?usp=sharing


## How to clone / install Pariby Test Automation
Open your terminal, go to your favorite directory for projects, type
git clone https://github.com/akarakus27/    
and hit enter. Pariby Test Automation will be cloned current directory.

After cloning, open Atlas project with PyCharm IDE and wait for first indexing progress. When indexing is finished, IDE auto detects requirements.txt file and asks for creating virtual environment. Click "OK" button, IDE will be created virtual environment and automatically installs required pip packages. From this point you can run tests, but you need one more thing, described in next step.

## How to run tests
python3 -m pytest test

## Configure Selenium Grid
* İnstall docker https://docs.docker.com/engine/install/ubuntu/

## Docker Network
Create a Docker Network
Use docker network create <NETWORK_NAME> command to create a network so that the containers can communicate with each other.
* docker network create grid
* List networks with docker network ls
## Create a Docker Hub
Use docker run to create a hub

"$ docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub:3.11.0-dysprosium"
d: detached mode. The container starts in the background with this command. You don’t see any output from the container console.

p: publish port (we bind the port 4444 of the container to 4444 of the docker host)

net: specify which network we add the container

name: specify a name of the container and the last parameter is the image name used when creating the container.

Now, list running containers by typing docker ps

Check http://localhost:4444/grid/console

## Create a Docker Node,
Let’s add one Chrome node:
$ docker run -d --net grid -e HUB_HOST=selenium-hub -v /dev/shm:/dev/shm selenium/node-chrome:3.11.0-dysprosium

Let’s add one Firefox node:

$ docker run -d --net grid -e HUB_HOST=selenium-hub -v /dev/shm:/dev/shm selenium/node-firefox:3.11.0-dysprosium



