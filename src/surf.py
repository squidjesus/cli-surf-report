import click
from pathlib import Path
from demo import load_demo_spots
from csv_funcs import create_spot_file
from callbacks import validate_ext_csv, validate_type_str
from surf_db_funcs import load_db, list_spots, add_spot, rm_spot


@click.group()
def surf():
    pass


# List surf spots in the database
@surf.command(help="Lists all saved surf spots, use '-d' or '--detail' to show additional spot details.")
@click.option('-d', '--detail', is_flag=True, help="Shows additional details")
def list(detail):
    db = load_db()
    list_spots(db, detail)
    db.close()
    exit(0)


# Add a surf spot
@surf.command(help="Add a surf spot to the database.")
def add():
    db = load_db()
    add_spot(db)
    db.close()
    exit(0)


# Remove a surf spot
@surf.command(help="Remove a surf spot from the database.")
@click.argument('name', help="surf spot name", callback=validate_type_str)
def remove(name):
    db = load_db()
    rm_spot(db, name)
    db.close()
    exit(0)


# Create a surf spots CSV file to import from
@surf.command(help="Format a new .csv file used for importing multiple surf spots. Usage: surf create-file 'C:/Temp/Surf_Spots.csv'")
@click.argument('filepath', type=click.Path(exists=False, dir_okay=False, resolve_path=True), callback=validate_ext_csv, help="Surf spot file path, usage: surf create-file 'C:/Temp/Surf_Spots.csv'")
def create_file(filepath):
    create_spot_file(filepath)
    click.echo(f"Created Surf Spots CSV file at {filepath}")
    exit(0)


# Import the 'demo' surf spots from data/surf_spots.csv
@surf.command(help="Populate the db with demo surf spots")
def demo_spots():
    db = load_db()
    if click.confirm("Add demo spots to the database?"):
        load_demo_spots(db)
    db.close()


@surf.command(help="Get the surf report for a given spot. Enter the --name. Get extended details with -d")
@click.option("-n", "name", help="Name of the surf spot, must match a spot name from the surf spots file")
@click.option("-d", "--detailed", help="Add this flag to see extended report with hourly forecast data")
def report(name, detail=None):

    click.echo(f"Getting report for: {name}")
    get_surf_report(name)
    surf_path = Path(config['spots_file_location'])



if __name__ == "__main__":
    surf()