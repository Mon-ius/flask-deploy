import re
import click

def validate_email(ctx, param, value):
    if not value:
        return
    try:
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                        value):
            raise ValueError(value)
        else:
            return value
    except ValueError as e:
        click.echo('Incorrect email address given: {}'.format(e))
        value = click.prompt(param.prompt)
        return validate_email(ctx, param, value)

def validate_domain(ctx, param, value):
    try:
        if not re.match(r"(^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$)",
                        value):
            raise ValueError(value)
        else:
            return value
    except ValueError as e:
        click.echo('Incorrect domain address given: {}'.format(e))
        value = click.prompt(param.prompt)
        return validate_domain(ctx, param, value)

def validate_options(ctx, param, value):
    if not value:
        return
    try:
        if not re.match(r"(^([0-1]))",
                        value) or len(value)>1:
            raise ValueError(value)
        else:
            return value
    except ValueError as e:
        click.echo('Incorrect options value given: {}'.format(e))
        value = click.prompt(param.prompt)
        return validate_options(ctx, param, value)
