import re
import click
import os
from .config import *


def ssl_file_gen(domain,usr,loc,email,key):
    with open(SSL, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{domain}}', '.'.join(domain.split('.')[-2:]), fds)
        fce = re.sub(r'{{EMAIL}}', email, fcd)
        res = re.sub(r'{{KEY}}', key, fce)

        with open(domain+"/"+domain+'.sh', 'w') as ssl_sh:
            ssl_sh.write(res)
            ssl_sh.close()
        fh.close()
        click.echo("-0- SSL script: {} create successfully".format(domain+"/"+domain+'.sh'))


def docker_file_gen(domain,usr,loc):
    with open(DOCKER, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{domain}}', domain, fds)
        fcu = re.sub(r'{{usr}}', usr, fcd)
        res = re.sub(r'{{passwd}}', loc+domain+usr, fcu)

        with open(domain+"/"+domain+'.run', 'w') as docker_run:
            docker_run.write(res)
            docker_run.close()

        fh.close()
        click.echo("-1- Docker config script: {} create successfully".format(domain+"/"+domain+'.run'))


def uwsgi_file_gen(domain,usr,loc):
    env = os.path.dirname(loc)
   
    with open(uWSGI, 'r') as fh:
        fds = fh.read()

        fce = re.sub(r'{{env}}',env+"/"+domain,fds)
        fcu = re.sub(r'{{usr}}',usr,fce)
        res = re.sub(r'{{loc}}',loc,fcu)

        with open(domain+"/"+domain+'.ini', 'w') as uwsgi_ini:
            uwsgi_ini.write(res)
            uwsgi_ini.close()
    
        fh.close()
        click.echo("-2- uwsgi config file: {} create successfully".format(domain+"/"+domain+'.ini'))

#static
def nginx_file_gen(domain,usr,loc):
    with open(NGINX, "r") as fh:
        fds = fh.read()
    
        fcd = re.sub(r'{{domain}}', domain, fds)
        res = re.sub(r'{{loc}}', loc, fcd)

        with open(domain+"/"+domain+'.conf', 'w') as nginx_conf:
            nginx_conf.write(res)
            nginx_conf.close()
        fh.close()

        click.echo("-3- Nginx config file: {} create successfully".format(domain+"/"+domain+'.conf'))

#static
def service_file_gen(domain,usr,loc):
    with open(SERVICE, "r") as fh:
        fds = fh.read()

        fcd = re.sub(r'{{domain}}', domain, fds)
        fcu = re.sub(r'{{usr}}', usr, fcd)
        res = re.sub(r'{{loc}}', loc, fcu)

        with open(domain+"/"+domain+'.service', 'w') as confservice:
            confservice.write(res)
            confservice.close()
        fh.close()
        click.echo("-4- Systemd service file : {} create successfully".format(domain+"/"+domain+'.service'))