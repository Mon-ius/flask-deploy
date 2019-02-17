from config import *
from validation import *
from utils import *

import subprocess
import getpass
import os
import click

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
    