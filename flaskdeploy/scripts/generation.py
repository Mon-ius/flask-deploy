import getpass
import os
import subprocess

import click

from ..config import *
from ..utils import *
from ..validation import *

# from .dns import *
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

@click.command(context_settings=dict(
    allow_extra_args=True
))
@click.option('--dns_type', prompt='Service options. \n [1] CloudFlare \n [2] AliYun \n\n\nYour Choice')
@click.pass_context
def miss_ssl(ctx,dns_type):
    """
    These are available DNS provider servie options. \n
    [1] CloudFlare <CF_Email,CF_Key> --dns dns_cf \n
    [2] AliYun <Ali_Key,Ali_Secret> --dns dns_ali \n
    """
    # if not dns_type:
    if(str(dns_type)=="1"):
        try:
            op_cf()
        except JumpOutFuckingClick2:
            pass
    if(str(dns_type)=="2"):
        try:
            op_ali()
        except JumpOutFuckingClick2:
            pass
    raise JumpOutFuckingClick
    

@click.command(short_help='AliYun Option',context_settings=dict(
    allow_extra_args=True
))
@click.option('--ali_key', prompt='Ali_Key')
@click.option('--ali_secret', prompt='Ali_Secret')
@click.pass_context
def op_ali(ctx,ali_key,ali_secret):
    dns_op = "dns_ali"
    op_1 = "Ali_Key={}".format(ali_key)
    op_2 = "Ali_Secret={}".format(ali_secret)
    ssl_multi_gen(DOMAIN, USR, CUR_LOC, op_1,op_2,dns_op)
    
    raise JumpOutFuckingClick2

@click.command(short_help='CloudFlare Option',context_settings=dict(
    allow_extra_args=True
))
@click.option('--cf_email', prompt='CF_Email')
@click.option('--cf_key', prompt='CF_Key')
@click.pass_context
def op_cf(ctx,cf_email,cf_key):
    dns_op = "dns_cf"
    op_1 = "CF_Email={}".format(cf_email)
    op_2 = "CF_Key={}".format(cf_key)
    ssl_multi_gen(DOMAIN, USR, CUR_LOC, op_1,op_2,dns_op)

    raise JumpOutFuckingClick2

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
    """Necessary config.(Just generating)"""
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
    script_files_gen(DOMAIN, USR, CUR_LOC)
