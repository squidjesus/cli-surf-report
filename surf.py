import click
import os
from csv_funcs import create_spot_file, list_spots, add_spot, load_spots, get_spot, validate_spots_csv
from pathlib import Path
from api_request_func import openmeteo_request
from report_class import Report
from config_funcs import load_config, save_config

@click.group()
def surf():
    pass


@surf.command(help="Create a new .csv file to hold surf spots. Usage: surf create --path 'C:/Temp/Surf_Spots.csv'")
@click.option("--path", type=click.Path(exists=False, dir_okay=False, resolve_path=True), help="Surf spot file path, usage: surf create --path 'C:/Temp/Surf_Spots.csv'")
def create(path):
    if not path:
        click.echo(click.style("ERROR: Path (for a new .csv file) required, example: --path 'C:/Temp/Surf_Spots.csv'", fg="red"))
        exit(1)
    if path[-4:] != ".csv":
        click.echo(click.style("ERROR: Must be a .csv file (path must end with .csv)", fg="red"))
        exit(1)
    if os.path.exists(path):
        click.echo(click.style("ERROR: File already exists.", fg="red"))
        exit(1)
    create_spot_file(path)
    click.echo("Created Surf Spots CSV file")

    if click.confirm(text="Set the new Surf Spots CSV as data source?"):
        config = load_config()
        config['spots_file_location'] = os.path.abspath(path)
        save_config(config)
        click.echo(f"Updated spots file to: {path}")


@surf.command(help="Set the surf spots CSV file to read from, you can use 'surf --create PATH' to create a blank CSV with the required fieldnames")
@click.option("--path", type=click.Path(exists=True, dir_okay=False, resolve_path=True))
def set(path):
    if path[-4:] != ".csv":
        click.echo(click.style("ERROR: Must be a .csv file (path must end with .csv)", fg="red"))
        exit(1)
    if not validate_spots_csv(path):
        click.secho("ERROR: CSV contains invalid fieldnames, see --help for formatting guide", fg="red")
        exit(1)
    config = load_config()
    config['spots_file_location'] = os.path.abspath(path)
    save_config(config)
    click.echo(f"Surf spots file set to: {path}")
    exit(0)


@surf.command(help="List all surf spot names in the current surf spots file, use '-d' or '--detail' to also show details.")
def list():
    config = load_config()
    list_spots(config['spots_file_location'])
    exit(0)


@surf.command(help="Add a spot to the current surf spots file.")
def add():
    config = load_config()
    if not config['spots_file_location']:
        click.secho("ERROR: Surf spots file not set, create one with 'surf spots-file --create PATH' or set with 'surf spots-file --set PATH'", fg="red")
        exit(1)
    spots_path = config['spots_file_location']
    click.echo(f"Add a surf spot to {spots_path}")
    new_spot = add_spot(spots_path)
    click.echo(f"Added {new_spot.name} to {spots_path}")
    exit(0)


@surf.command(help="Get the surf report for a given spot. Enter the --name. Get extended details with -d")
@click.option("-n", "name", help="Name of the surf spot, must match a spot name from the surf spots file")
@click.option("-d", "--detailed", help="Add this flag to see extended report with hourly forecast data")
def report(name, detail=None):
    click.echo(f"Welcome to CLI-Surf-Report!")
    config = load_config()
    if not config['spots_file_location']:
        click.secho("ERROR: Surf spots file not set, create one with 'surf spots-file --create PATH' or set with 'surf spots-file --set PATH'", fg="red")
        exit(1)
    click.echo(f"Getting report for: {name}")
    get_surf_report(name)
    surf_path = Path(config['spots_file_location'])



if __name__ == "__main__":
    surf()