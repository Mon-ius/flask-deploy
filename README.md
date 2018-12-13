# flask-deploy
A simple scripts for deploying flask apps with Nginx, PostgreSQL , HTTPS and Systemd Daemon.

## Assumptions

- You're user : `www`
- You have experience with Linux

## requirements

Assumed you have these following conditions.

### OutSide

- server
    - `example : centos`

    - ip address : 

- domain
    - `example : www.example.com`

- DNS
    - redirect <domain> => <ip>


### Software and enviroment

- git
- wget
- curl
- Nginx
- docker-ce
- Anaconda3
- Python3.6+
- uWSGI
- Gevnet

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


## Attention

### Ubuntu 18.x

- docker-ce install 

`sudo apt install apt-transport-https ca-certificates curl software-properties-common`
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"`
`sudo apt install docker-ce`

## Options

### Anaconda environment

Suppose location : `/opt/anaconda3`

- sudo chown -R www:www /opt/ && cd /opt
- wget "https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh"
- sudo chmod +x ./Anaconda3-5.3.1-Linux-x86_64.sh && ./Anaconda3-5.3.1-Linux-x86_64.sh
- following the tips: `yes` - `/opt/anaconda3` - `yes`

### Anaconda setup

- conda create -n deploy python=3.6
- conda activate deploy
- conda install -c conda-forge gevent
- conda install -c conda-forge uwsgi

## MIT License

Copyright (c) 2018 Monius

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.