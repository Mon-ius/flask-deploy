from config import *
from validation import *
from utils import *

import subprocess
import getpass
import os
import click

@click.group()
def cx():
    """A quick deploy script for productive flask app."""

@cx.command()
@click.option('--email', prompt='Your email', help='Email,Apply ssl certification,CloudFlare.',
              callback=validate_email)
@click.option('--key', prompt='Your secret key', help='Secret Key,Apply ssl certification,CloudFlare.')
def miss_tmp(email, key):
    ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)

@cx.command('deploy', short_help='deploy the app')
@click.option('--domain', prompt='Your domain', help='The domain to be configured.',
              callback=validate_domain
              )
@click.option('--email', help='Email,Apply ssl certification,CloudFlare.',
              callback=validate_email
              )
@click.option('--key', help='Key,Apply ssl certification,CloudFlare.')
@click.option('--docker', help='Confirm having database or not.')
@click.pass_context
def deploy(ctx, domain, email, key,docker):
    """Deploy the flask app right now."""
    global DOMAIN, USR, CUR_LOC
    usr = getpass.getuser()
    loc = os.path.join(os.getcwd(), domain)
    DOMAIN, USR, CUR_LOC = domain, usr, loc

    if not os.path.exists(CUR_LOC):
        try:
            os.makedirs(CUR_LOC)
        except:
            if click.confirm("You have no privilege of current location Would you like to own it?"):
                subprocess.call(['sudo', 'chown', '-R', usr+":"+usr, './'])
                os.makedirs(loc)
            else:
                click.echo("You have no previlege!!!")
                return

    uwsgi_file_gen(DOMAIN, USR, CUR_LOC)
    nginx_file_gen(DOMAIN, USR, CUR_LOC)
    service_file_gen(DOMAIN, USR, CUR_LOC)

    if not docker:
        if not click.confirm('Do you have database already?'):
            docker_file_gen(DOMAIN, USR, CUR_LOC)
    if not email or not key:
        if not click.confirm('Do you have SSL certification?'):
            miss_tmp()
    else:
        ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)

    script_files_gen(DOMAIN, USR, CUR_LOC)

@cx.command('gen', short_help='gen the config')
@click.option('--domain', prompt='Your domain', help='The domain to be configured.',
              callback=validate_domain
              )
@click.option('--email', help='Email,Apply ssl certification,CloudFlare.',
              callback=validate_email
              )
@click.option('--key', help='Key,Apply ssl certification,CloudFlare.')
@click.option('--docker', help='Confirm having database or not.')
@click.pass_context
def gen(ctx, domain, email, key,docker):
    """Generates the necessary config.(Just generating)"""
    global DOMAIN, USR, CUR_LOC
    usr = getpass.getuser()
    loc = os.path.join(os.getcwd(), domain)
    DOMAIN, USR, CUR_LOC = domain, usr, loc

    if not os.path.exists(CUR_LOC):
        try:
            os.makedirs(CUR_LOC)
        except:
            if click.confirm("You have no privilege of current location Would you like to own it?"):
                subprocess.call(['sudo', 'chown', '-R', usr+":"+usr, './'])
                os.makedirs(loc)
            else:
                click.echo("You have no previlege!!!")
                return

    uwsgi_file_gen(DOMAIN, USR, CUR_LOC)
    nginx_file_gen(DOMAIN, USR, CUR_LOC)
    service_file_gen(DOMAIN, USR, CUR_LOC)

    if not docker:
        if not click.confirm('Do you have database already?'):
            docker_file_gen(DOMAIN, USR, CUR_LOC)
    if not email or not key:
        if not click.confirm('Do you have SSL certification?'):
            miss_tmp()
    else:
        ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)

# @cx.command('gen', short_help='gen the config')
# def gen():
#     """Generates the necessary config.(Just generating)"""

# @cx.command('deploy', short_help='deploy the app')
# def deploy():
#     """Deploy the flask app right now."""

if __name__ == '__main__':
    cx()
