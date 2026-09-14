import click

def validate_ext_csv(ctx, param, value):
    if value and not value.endswith(".csv"):
        raise click.BadParameter("Must be a .csv")
    return value