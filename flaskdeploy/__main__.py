import click
from flaskdeploy.scripts import deploy,gen


@click.group()
def cli():
    pass


cli.add_command(deploy.cli, 'deploy')
cli.add_command(gen.cli, 'gen')


# Enable ``python -m flask-deploy ...``.
if __name__ == '__main__':  # pragma: no cover
    cli()
