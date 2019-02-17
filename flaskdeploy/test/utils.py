import re
import click
import os
from config import *

class JumpOutFuckingClick(Exception):
   """Just to break out the unkown loop"""
   pass

class JumpOutFuckingClick2(Exception):
   """Just to break out the unkown loop2"""
   pass

def ssl_file_gen(domain,usr,loc,email,key):
    with open(SSL, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{DOMAIN}}', '.'.join(domain.split('.')[-2:]), fds)
        fce = re.sub(r'{{EMAIL}}', email, fcd)
        res = re.sub(r'{{KEY}}', key, fce)

        with open(domain+"/"+domain+'.sh', 'w') as ssl_sh:
            ssl_sh.write(res)
            ssl_sh.close()
        fh.close()
        click.echo("-4- SSL script: {} create successfully".format(domain+"/"+domain+'.sh'))

def ssl_multi_gen(domain,usr,loc,op1,op2,dns_op):
    with open(SSL, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{DOMAIN}}', '.'.join(domain.split('.')[-2:]), fds)
        fce = re.sub(r'{{OP1}}', op1, fcd)
        fcf = re.sub(r'{{OP2}}', op2, fce)
        res = re.sub(r'{{DNS_OP}}', dns_op, fcf)

        with open(domain+"/"+domain+'.sh', 'w') as ssl_sh:
            ssl_sh.write(res)
            ssl_sh.close()
        fh.close()
        click.echo("-4- SSL script: {} create successfully".format(domain+"/"+domain+'.sh'))


def docker_file_gen(domain,usr,loc):
    with open(DOCKER, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{DOMAIN}}', domain, fds)
        fcu = re.sub(r'{{usr}}', usr, fcd)
        res = re.sub(r'{{passwd}}', loc+domain+usr, fcu)

        with open(domain+"/"+domain+'.run', 'w') as docker_run:
            docker_run.write(res)
            docker_run.close()

        fh.close()
        click.echo("-3- Docker config script: {} create successfully".format(domain+"/"+domain+'.run'))


def uwsgi_file_gen(domain,usr,loc):
    env = os.path.dirname(loc)
   
    with open(uWSGI, 'r') as fh:
        fds = fh.read()

        fce = re.sub(r'{{env}}',env,fds)
        fcu = re.sub(r'{{usr}}',usr,fce)
        res = re.sub(r'{{loc}}',loc,fcu)

        with open(domain+"/"+domain+'.ini', 'w') as uwsgi_ini:
            uwsgi_ini.write(res)
            uwsgi_ini.close()
    
        fh.close()
        click.echo("-0- uwsgi config file: {} create successfully".format(domain+"/"+domain+'.ini'))

#static
def nginx_file_gen(domain,usr,loc):
    with open(NGINX, "r") as fh:
        fds = fh.read()
    
        fcd = re.sub(r'{{DOMAIN}}', domain, fds)
        res = re.sub(r'{{loc}}', loc, fcd)

        with open(domain+"/"+domain+'.conf', 'w') as nginx_conf:
            nginx_conf.write(res)
            nginx_conf.close()
        fh.close()

        click.echo("-1- Nginx config file: {} create successfully".format(domain+"/"+domain+'.conf'))

#static
def service_file_gen(domain,usr,loc):
    with open(SERVICE, "r") as fh:
        fds = fh.read()

        fcd = re.sub(r'{{DOMAIN}}', domain, fds)
        fcu = re.sub(r'{{usr}}', usr, fcd)
        res = re.sub(r'{{loc}}', loc, fcu)

        with open(domain+"/"+domain+'.service', 'w') as confservice:
            confservice.write(res)
            confservice.close()
        fh.close()
        click.echo("-2- Systemd service file : {} create successfully".format(domain+"/"+domain+'.service'))


def script_files_gen(domain, usr, loc):
    cmd = []
    files = loc+"/"+domain
    c = None
    if os.path.exists(files+'.sh'):
        c = "sudo mkdir /etc/nginx/certs"
        c1 = "sudo "+files+'.sh'

        cmd.append(c)
        cmd.append(c1)

    if os.path.exists(files+'.run'):
        c = "sudo "+files+'.run'
        cmd.append(c)

    if os.path.exists(files+'.conf'):
        c = "sudo cp "+files+'.conf ' + NGINX_CONF1
        c1 = "sudo cp "+files+'.conf ' + NGINX_CONF2
        c2 = "sudo nginx -s reload"
        cmd.append(c)
        cmd.append(c1)
        cmd.append(c2)

    if os.path.exists(files+'.service'):
        c = "sudo cp "+files+'.service ' + SYSTEMD_CONF
        c1 = "sudo systemctl enable "+domain+'.service'
        c2 = "sudo systemctl start "+domain+'.service'
        cmd.append(c)
        cmd.append(c1)
        cmd.append(c2)

    with open(loc+'/start.sh', 'w') as file:
        for c in cmd:
            file.write(c+"\n")
        file.close()
    click.echo("-5- One click script file : {} create successfully".format(domain+"/"+'start.sh'))
