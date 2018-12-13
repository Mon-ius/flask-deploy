import click
from flaskdeploy.scripts import deploy,gen


@click.group()
def cli():
    """A quick deploy script for productive flask app."""
    pass


cli.add_command(deploy.cli, 'deploy', short_help='deploy the app')
cli.add_command(gen.cli, 'gen', short_help='gen the config')



# Enable ``python -m flask-deploy ...``.
if __name__ == '__main__':  # pragma: no cover
    cli()
