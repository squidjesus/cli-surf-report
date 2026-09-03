import click
from surf_spots_ import create_spot_file, list_spots, add_spot, load_spots
from pathlib import Path


@click.command()
@click.option("--read", is_flag=True)
@click.option("-a", "--add", is_flag=True, help="Add a surf spot: respond to the prompts to enter Nickname, Latitude, Longitude, Optimal Swell Dir. and Optimal Wind Dir.")
@click.option("-l", "--load",
              type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True, readable=True), 
              help="Path to your surf spots csv, use --format or -f to show .csv file formatting"
              )
@click.option("-f", "--format", is_flag=True, help="Shows .csv formatting for bulk surf spots loading")
@click.option("-r", "--report", is_flag=True)
def surf(read, add, load, format, report):

    surf_path = Path("surf_spots.csv")

    if read:
        if not surf_path.exists():
            click.echo("No spots file found, add a spot with '--add', or import a surf spots .csv with '--load', (see '--format' for formatting guide)")
            return
        
        for spot in list_spots(surf_path):
            click.echo(spot)
        return

    if add:
        if not surf_path.exists():
            create_spot_file(surf_path)
        
        new_spot = {
            'name' : click.prompt("Surf Spot name"),
            'type' : click.prompt("Break type (reef, point, beach etc.)"),
            'lat'  : click.prompt("Latitude (to 4 dec places '1.1234')"),
            'long' : click.prompt("Longitude (to 4 dec places '1.1234')"),
            'opt_swells' : click.prompt("Optimal swell direction(s) separate by space ex. -> N NE NNE"),
            'opt_wind'   : click.prompt("Optimal wind direction ex. -> S"),
            'opt_tide'   : click.prompt("Optimal tide"),
            'notes'      : click.prompt("Notes")
        }
        add_spot(surf_path, new_spot)
        click.echo(f"Added spot: {new_spot['name']}")
        return

    if load:
        if not surf_path.exists():
            create_spot_file(surf_path)

        spots_to_load = Path(click.prompt("Path to csv file: "))
        spots_loaded = load_spots(surf_path, spots_to_load)

        click.echo(f"Loaded external file and added {spots_loaded} surf spots!")
        return

if __name__ == "__main__":
    surf()