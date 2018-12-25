from ..config import *
from ..validation import *
from ..utils import *

import subprocess
import getpass
import os

import click

@click.command()
@click.option('--domain', prompt='Your domain', help='The domain to be configured.',
              callback=validate_domain)
@click.pass_context
def cli(ctx, domain):
    """Run generated script: startup.sh"""
    global DOMAIN, USR, CUR_LOC
    usr = getpass.getuser()
    loc = os.path.join(os.getcwd(), domain)
    DOMAIN, USR, CUR_LOC = domain, usr, loc

    
    if not os.path.exists(CUR_LOC):
        click.echo("No folder for domain({}) at user({}) environment, please try fd/flask-deploy generate to init.".format(DOMAIN,USR))
        return
    else:
        try:
            current_files = os.listdir(CUR_LOC)
            if "start.sh" in current_files:
                script_files_run(DOMAIN, USR, CUR_LOC)
                return
            else:
                click.echo("No file for domain({}) at user({}) environment, please try fd/flask-deploy generate to init.".format(CUR_LOC,USR))
                return
        except:
            if click.confirm("You have no privilege of current location Would you like to own it?"):
                subprocess.call(['sudo', 'chown', '-R', USR+":"+USR, './'])
                os.makedirs(loc)
            else:
                click.echo("You have no previlege!!!")
                return
