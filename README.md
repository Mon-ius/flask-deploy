# flask-deploy
A simple scripts for deploying flask apps with Nginx, PostgreSQL , HTTPS and Systemd Daemon.

## requirements

Assumed you meet these following conditions.

- Linux kernel >= 3.13.
- Conda environment.
- Python 3.6+
- Ngnix
- Docker
- Domain.

## Start

Following these steps, then select things you want. All of things will be generated.

- create a user (For example : www)
- Switch to python virtual env
- python init.py

Then change to ROOT or sudoer with following things.

## Get SSL

- Run ``` sudo ./domain.sh ```

It will generate the certifications(.cer,.key) for your project if you first run it.

## Configure nginx for FLASK Application

- ``` sudo mv ./domain.conf /etc/nginx/sites-enabled```

It will add the configuration file to NGINX for your project if you first run it.

## Run FLASK Application as Systemd Daemon

- ``` sudo mv ./domain.service /etc/systemd/system```
- sudo systemctl enable domain
- sudo systemctl start domain

It will add the service file to Systemd and make your project run as system service if you first run it.

Then you could manage it by:
- sudo systemctl stop domain
- sudo systemctl restart domain

