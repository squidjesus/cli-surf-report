import click
import os
from spots_csv import create_spot_file, list_spots, add_spot, load_spots, get_spot
from pathlib import Path
from request import openmeteo_request
from report import Report
from config_funcs import load_config, save_config

#@click.option("-d", "--display", default="all", help="Spot name, in quotations if there are spaces")
#@click.option("-a", "--add", is_flag=True, help="Add a surf spot: respond to the prompts to enter Nickname, Latitude, Longitude, Optimal Swell Dir. and Optimal Wind Dir.")
#@click.option("-c", "--copy", type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True, readable=True), help="Path to your surf spots csv, use --format or -f to show .csv file formatting")
#@click.option("-f", "--format", is_flag=True, help="Shows .csv formatting for bulk surf spots loading")
#@click.option("-r", "--report", help="Print the surf report for the specified SURF_SPOT")

@click.group()
def surf():
    pass

@click.command(help="Create a new .csv file to hold surf spots. Usage: surf create --path 'C:/Temp/Surf_Spots.csv'")
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


@click.command()
@click.option("--path", type=click.Path(exists=True, dir_okay=False, resolve_path=True), help="Set the surf spots CSV file to read from. you can use 'surf --create PATH' to create a blank CSV with the required fieldnames")
def set(path):
    config = load_config()
    config['spots_file_location'] = os.path.abspath(path)
    save_config(config)
    click.echo(f"Surf spots file set to: {path}")

@click.command(help="List all surf spot names in the current surf spots file, use '-d' or '--detail' to also show details.")
def list():
    config = load_config()
    list_spots(config['spots_file_location'])

@click.command()
def report():
    click.echo(f"Welcome to CLI-Surf-Report!")
    config = load_config()
    if not config['spots_file_location']:
        click.echo("Surf spots file set, create one with 'surf spots-file --create PATH' or set with 'surf spots-file --set PATH'")
        return
    click.echo(f"Loading Spots File: {config['spots_file_location']}")
    surf_path = Path(config['spots_file_location'])

    

    if display:
        if not surf_path.exists():
            click.echo("No spots file found, add a spot with '--add', or import a surf spots .csv with '--load', (see '--format' for formatting guide)")
            return
        list_spots(surf_path, display)
        return

    if add:
        if not surf_path.exists():
            create_spot_file(surf_path)
        
        new_spot = {
            'name' : click.prompt("Surf Spot name"),
            'city' : click.prompt("City"),
            'state': click.prompt("State"),
            'type' : click.prompt("Break type (reef, point, beach etc.)"),
            'lat'  : click.prompt("Latitude (to 4 dec places '1.1234')"),
            'long' : click.prompt("Longitude (to 4 dec places '-1.1234')"),
            'opt_swells' : click.prompt("Optimal swell direction(s) separate by comma ex. -> N,NE,NNE").strip().replace(" ",""),
            'opt_wind'   : click.prompt("Optimal wind direction ex. -> S"),
            'notes'      : click.prompt("Notes")
        }
        add_spot(surf_path, new_spot)
        click.echo(f"Added spot: {new_spot['name']}")
        return

    if copy:
        if not surf_path.exists():
            create_spot_file(surf_path)
        spots_loaded = load_spots(surf_path, copy)
        click.echo(f"Loaded external file and added {spots_loaded} surf spots!")
        return

    if report:
        surf_spot = get_spot(surf_path, report)
        responses = openmeteo_request(surf_spot)
        surf_spot_report = Report(responses, surf_spot)
        click.echo(surf_spot_report)
        return

#Command Groups Attaching
surf.add_command(create)
surf.add_command(set)

if __name__ == "__main__":
    surf()