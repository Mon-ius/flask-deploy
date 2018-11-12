# Steps to deploy

- ubuntu 18.04 (x64)
- python 3.7

## Basic

### add user(example : www)

- sudo adduser www && sudo usermod -G sudo www
- sudo chown -R www:www /opt/ && su www 
- cd ~

### zsh (recommend!!)

- sudo apt install zsh
- sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
- chsh -s /bin/zsh

### conda environment

- wget "https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh"
- sudo chmod +x ./Anaconda3-5.3.0-Linux-x86_64.sh && ./Anaconda3-5.3.0-Linux-x86_64.sh

- conda create -n deploy python=3.7
- echo "alias deploy='conda activate deploy'" >> ~/.zshrc && source ~/.zshrc && deploy
- conda install -c conda-forge uwsgi gevent
- conda install --yes --file requirements.txt

### Nginx

- sudo apt install nginx
- nginx -t
- nginx -s reload

## Ultimate

### SSL configuration 

### Systemd Service

### Docker based Postgres Database

docker run --name IOTBASE -d -p 5432:5432 -v ~/Postgres:/var/lib/postgresql/data -e POSTGRES_DB=iot -e POSTGRES_USER={{usr}} -e POSTGRES_PASSWORD='{{passwd}}' postgres:latest

CREATE DATABASE {{database_name}} OWNER {{user}};
GRANT ALL PRIVILEGES ON DATABASE {{database_name}} to {{user}};

### python-dotenv

pip install python-dotenv
- ``` load_dotenv(os.path.join(basedir, '.env')) ```


## Auto deploy script

### enviroment

- domain name(*)
- SSL email(*)
- SSL API key(*)
- current user(-)
- current folder(-)
- current project folder(-)
- current project name(-)

### SSL

- sudo apt install socat

### uwsgi.ini

### nginx.conf

### docker script

- sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
- sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
- sudo apt update && sudo apt install docker-ce -y


### iot.service

/etc/systemd/system

- sudo systemctl enable iot
- sudo systemctl start iot
- sudo journalctl -u [unit]
