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

@click.command(context_settings=dict(
    allow_extra_args=True
))
@click.option('--email', prompt='Your email', help='Email,Apply ssl certification,CloudFlare.',
              callback=validate_email)
@click.option('--key', prompt='Your secret key', help='Secret Key,Apply ssl certification,CloudFlare.')
@click.option('--domain')
@click.pass_context
def miss_tmp(ctx,email, key,domain):
    ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)
    raise JumpOutFuckingClick

@click.command()
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
            try:
                miss_tmp()
            except JumpOutFuckingClick:
                pass
    else:
        ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)

    script_files_gen(DOMAIN, USR, CUR_LOC)


@click.command()
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
    if not email or not key:
        if not click.confirm('Do you have SSL certification?'):
            try:
                miss_tmp()
            except JumpOutFuckingClick:
                click.echo("2333")
    else:
        ssl_file_gen(DOMAIN, USR, CUR_LOC, email, key)



@click.command()
@click.option('--domain', prompt='Your domain', help='The domain to be configured.',
              callback=validate_domain)
@click.pass_context
def run(ctx, domain):
    """Run generated script: startup.sh"""
    global DOMAIN, USR, CUR_LOC
    usr = getpass.getuser()
    loc = os.path.join(os.getcwd(), domain)
    DOMAIN, USR, CUR_LOC = domain, usr, loc

    
    if not os.path.exists(CUR_LOC):
        click.echo("No folder for domain({}) at user({}) environment, please try fd/flask-deploy generate to init.".format(domain,usr))
        return
    else:
        try:
            current_files = os.listdir(CUR_LOC)
            if "start.sh" in current_files:
                click.echo("On load")
                return
            else:
                click.echo("No file for domain({}) at user({}) environment, please try fd/flask-deploy generate to init.".format(CUR_LOC,usr))
                return
        except:
            if click.confirm("You have no privilege of current location Would you like to own it?"):
                subprocess.call(['sudo', 'chown', '-R', usr+":"+usr, './'])
                os.makedirs(loc)
            else:
                click.echo("You have no previlege!!!")
                return

cli = click.Group()
@click.command(short_help='test',context_settings=dict(
    allow_extra_args=True
))
@click.option('--count', prompt='count')
def test(count):
    click.echo('Count: {}'.format(count))
    raise JumpOutFuckingClick


@click.command(short_help='dist')
@click.option('--count')
@click.pass_context
def dist(ctx, count):
    if not count:
        try:
            test()
        except JumpOutFuckingClick:
            click.echo("2333")

# cli.add_command(dist, 'dist')
# cli.add_command(test, 'test')

cx.add_command(gen, 'gen')
cx.add_command(deploy, 'deploy')
cx.add_command(run, 'run')

if __name__ == '__main__':
    # cli()
    cx()
