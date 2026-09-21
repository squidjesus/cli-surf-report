import click
from src.report_class import Report
from src.demo import load_demo_spots
from src.report_funcs import data_to_table
from src.csv_funcs import create_spot_file
from src.api_request import openmeteo_request
from src.callbacks import validate_ext_csv, validate_type_str
from src.surf_db_funcs import load_db, list_spots, add_spot, rm_spot, get_spot, get_all_spots


@click.group()
def surf():
    pass

@surf.command(help="Get the surf report for given spots")
@click.option('-a', '--all', is_flag=True, default=False)
@click.argument('spots', nargs=-1, default=['all'], required=False, help="Name(s) of surf spots to report, must match 'name' from the database")
def report(all, spots):
    db = load_db()
    if all or spots[0] == 'all':
        spots = get_all_spots(db)
    reports = []
    colors = []
    for s in spots:
        spot = get_spot(db, s)
        if spot == None:
            continue
        api_req = openmeteo_request(spot)
        report = Report(api_req, spot)
        reports.append(report)
    data_to_table(reports)

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


if __name__ == "__main__":
    surf()