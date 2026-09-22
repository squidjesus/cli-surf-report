import click

def validate_ext_csv(ctx, param, value):
    if value and not value.endswith(".csv"):
        raise click.BadParameter("Must be a .csv")
    return value

def validate_type_str(ctx, param, value):
    if value and not isinstance(value, str):
        raise click.BadParameter("Expecting a name, must be a string")
    return value
