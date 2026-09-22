import click
from rich_functions import get_reports, print_table
from callbacks import validate_type_str
from database_functions import load_db, list_spots, add_spot, rm_spot, get_spot, get_all_spots, load_demo_spots


@click.group()
def surf():
    """
    Check the current surf conditions at your favorite spots!

    Try it out with: 'surf report' (On first run, choose option 1 to load the included demo spots) 

    Weather/Marine data provided by Open-Meteo. 
    """
    pass

# Print surf report for current conditions
@surf.command(help="Get the surf report for given spots, leave [SPOTS] blank to include all")
@click.option('-a', '--all', is_flag=True, default=False, help="Print the report for all spots in the database")
@click.argument('spots', nargs=-1, default=['all'], required=False, help="Name(s) of surf spots to report, must match 'name' from the database")
def report(all, spots):
    db = load_db()
    if all or spots[0] == 'all':
        spots = get_all_spots(db)
    reports = get_reports(spots, db)
    print_table(reports)


# List surf spots in the database
@surf.command(help="List saved surf spots, defaults to 'all', use '-d' or '--detail' to show additional spot details.")
@click.option('-d', '--detail', is_flag=True, default=False, help="Shows all spot details")
@click.option('-a', '--all', is_flag=True, default=False, help="List all spots in the database")
@click.argument('spots', nargs=-1, default=['all'], required=False, help="Name(s) of surf spots to list, must match 'name' from the database")
def list(detail, all, spots):
    db = load_db()
    if all or spots[0] == 'all':
        list_spots(db, detail)
    else:
        list_spots(db, detail, spots)
    db.close()
    exit(0)


# Add a surf spot
@surf.command(help="Add a surf spot to the database by responding to the prompts. Use Google Maps to find the lat/long for custom spots")
def add():
    db = load_db()
    add_spot(db)
    db.close()
    exit(0)


# Remove a surf spot
@surf.command(help="Remove a given surf spot [NAME] from the database.")
@click.argument('name', help="surf spot name", callback=validate_type_str)
def remove(name):
    db = load_db()
    rm_spot(db, name)
    db.close()
    exit(0)


# Import the 'demo' surf spots from data/surf_spots.csv
@surf.command(help="Populate the db with the demo surf spots from data/demo_surf_spots.csv")
def demo_spots():
    demo = True
    db = load_db(demo)
    db.close()


if __name__ == "__main__":
    surf()