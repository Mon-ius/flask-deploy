from scripts.config import *
import getpass
import subprocess
import os
import re


def accept_warning(s):
    c = ''
    d = {'Y': True, 'y': True, 'N': False, 'n': False}
    while not c in d:
        c = input('Warning: %s \n Y/N? ' % s)
    return d[c]


def get_env():
    domain = input("Input domain : ")
    usr = getpass.getuser()
    loc = os.getcwd()+"/"+domain
    # cmd = "mkdir "+domain
    # print(cmd)
    # subprocess.call(['sudo', 'mkdir', domain])
    if not os.path.exists(loc):
        try:
            os.makedirs(loc)
        except:
            if accept_warning("You have no privilege of current location Would you like to own it?"):
                subprocess.call(['sudo', 'chown', '-R',usr+":"+usr,'./'])
                os.makedirs(loc)
            else:
                print("You have no previlege!!!")
                os._exit(0)

    return domain,usr,loc

def add_env(**args):
    env = os.path.dirname(os.path.dirname(loc))
    print(args)
    with open(env+'/.env', 'a') as file:
        for i,j in args.items():
            tmp = i+'='+j
            print(tmp)
            file.write(tmp)
        file.close()
    return False

def ssl_file_gen(domain,usr,loc):
    if accept_warning("Do you have ssl cert?"):
        return
    key = input("Cloudflare API toke : ")
    email = input("Cloudflare email : ")
    
    with open(SSL, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{domain}}', '.'.join(domain.split('.')[-2:]), fds)
        fce = re.sub(r'{{EMAIL}}', email, fcd)
        res = re.sub(r'{{KEY}}', key, fce)

        with open(domain+"/"+domain+'.sh', 'w') as ssl_sh:
            ssl_sh.write(res)
            ssl_sh.close()
        fh.close()

    # with open(domain+'/start.sh', 'a') as file:
    #     cmd = "sudo mkdir /etc/nginx/certs"
    #     file.write(cmd)
    #     file.close()
    #     if not os.path.exists("/etc/nginx/certs"):
    #         os.makedirs("/etc/nginx/certs")
    #     os.chmod(domain+'.sh', 0o700)

    #     # os.system(domain+'.sh')
    #     # os.remove(domain+'.sh')

        print("-0- SSL script: {} create successfully".format(domain+"/"+domain+'.sh'))


def docker_file_gen(domain,usr,loc):
    if accept_warning("Do you have database already?"):
        return
    with open(DOCKER, "r") as fh:
        fds = fh.read()
        fcd = re.sub(r'{{domain}}', domain, fds)
        fcu = re.sub(r'{{usr}}', usr, fcd)
        res = re.sub(r'{{passwd}}', loc+domain+usr, fcu)

        with open(domain+"/"+domain+'.run', 'w') as docker_run:
            docker_run.write(res)
            docker_run.close()

        fh.close()

        # os.chmod(domain+'.run', 0o700)
        # os.system(domain+'.run')
        # os.remove(domain+'.run')

        #add DATABASE_URL into .env
        # conf = "postgres://{}:{}@172.17.0.1:5432/{}".format(usr, loc+domain+usr, domain)
        # add_env(DATABASE_URL=conf)

        print("-1- Docker config script: {} create successfully".format(domain+"/"+domain+'.run'))
        # print("-1- Enviroment file : {} add successfully".format("app/.env"))

def uwsgi_file_gen(domain,usr,loc):
    env = os.path.dirname(os.path.dirname(loc))
   
    with open(uWSGI, 'r') as fh:
        fds = fh.read()

        fce = re.sub(r'{{env}}',env+"/"+domain,fds)
        fcu = re.sub(r'{{usr}}',usr,fce)
        res = re.sub(r'{{loc}}',loc,fcu)

        with open(domain+"/"+domain+'.ini', 'w') as uwsgi_ini:
            uwsgi_ini.write(res)
            uwsgi_ini.close()
    
        fh.close()
        print("-2- uwsgi config file: {} create successfully".format(domain+"/"+domain+'.ini'))

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

        print("-3- Nginx config file: {} create successfully".format(domain+"/"+domain+'.conf'))


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
        #reload deamon
        fh.close()
        print("-4- Systemd service file : {} create successfully".format(domain+"/"+domain+'.service'))

def config_files_gen(domain,usr,loc):
    ssl_file_gen(domain,usr,loc)
    docker_file_gen(domain,usr,loc)
    uwsgi_file_gen(domain,usr,loc)
    nginx_file_gen(domain,usr,loc)
    service_file_gen(domain,usr,loc)

def script_files_gen(domain,usr,loc):
    cmd =[]
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
        c = "sudo cp "+files+'.conf '+ NGINX_CONF1
        c1 = "sudo cp "+files+'.conf '+ NGINX_CONF2
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


def script_files_run(domain, usr, loc):
    subprocess.call(['sudo', loc+'/start.sh'])

if __name__ == '__main__':
    domain,usr,loc = get_env()
    
    config_files_gen(domain, usr, loc)
    # script_files_gen(domain, usr, loc)
    # script_files_run(domain, usr, loc)

    
    # add_uwsgi(usr,loc)
    # add_nginx(loc)
    # add_service(usr,loc)
