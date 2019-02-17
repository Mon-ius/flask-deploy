from ..config import *
from ..validation import *
from ..utils import *

from .dns import *

import subprocess
import getpass
import os

import click

# @click.command(context_settings=dict(
#     allow_extra_args=True
# ))
# @click.option('--email', prompt='Your email', help='Email,Apply ssl certification,CloudFlare.',
#               callback=validate_email)
# @click.option('--key', prompt='Your secret key', help='Secret Key,Apply ssl certification,CloudFlare.')
# @click.option('--domain')
# @click.pass_context
# def miss_tmp(ctx,email, key,domain):
#     ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)
#     raise JumpOutFuckingClick


@click.command()
@click.option('--domain', prompt='Your domain', help='The domain to be configured.',
              callback=validate_domain
              )
@click.option('--dns_option', help='DNS option,Apply ssl certification. \n[1]CloudFlare,\n[2]AliYun.',
              callback=validate_options
              )
@click.option('--docker', help='Confirm having database or not.')
@click.pass_context
def cli(ctx, domain, dns_option,docker):
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
    if not dns_option:
        if not click.confirm('Do you have SSL certification?'):
            try:
                # miss_tmp()
                miss_ssl()
            except JumpOutFuckingClick:
                pass
    else:
        if(str(dns_option)=="1"):
            try:
                op_cf()
            except JumpOutFuckingClick2:
                pass
        if(str(dns_option)=="2"):
            try:
                op_ali()
            except JumpOutFuckingClick2:
                pass
                
    script_files_run(DOMAIN, USR, CUR_LOC)