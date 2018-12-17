from .deploy import cli as deploy
from .generation import cli as generation

import click

@click.group()
def cli():
    """A quick deploy script for productive flask app."""
    pass


cli.add_command(deploy, 'deploy')
cli.add_command(generation, 'gen')
