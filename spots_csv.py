import csv
import click
from pathlib import Path
from surf_spot import Surf_Spot

FIELDS = ['name', 'city', 'state', 'type', 'lat', 'long', 'opt_swells', 'opt_wind', 'notes']

# Create "surf_spots.csv" in the root folder with the appropriate field names
def create_spot_file(surf_spots: Path):
    with open(surf_spots, mode="w", newline="") as file:
        spots_writer = csv.DictWriter(file, fieldnames=FIELDS)
        spots_writer.writeheader()

# Initializes surf spots from the CSV and prints them to the console
def list_spots(surf_spots: Path):
    with open(surf_spots, mode='r') as file:
        spots_read = csv.DictReader(file)
        i = 1
        for spot in spots_read:
            current_spot = Surf_Spot(**spot)
            click.echo(f"{i}. {current_spot.name}: {current_spot.city}, {current_spot.state}")
            i += 1
        return
        
# Adds a surf spot to the CSV
def add_spot(surf_spots: Path, new_spot: dict):
    with open(surf_spots, mode='a', newline='') as file:
        spots_write = csv.DictWriter(file, fieldnames=FIELDS)
        spots_write.writerow(new_spot)
    return

# Copies spots from an external surf spots CSV to "surf_spots.csv"
def load_spots(surf_spots: Path, to_import: Path) -> int:
    count = 0

    with open(to_import, mode="r", newline="") as infile, \
         open(surf_spots, mode="a", newline="") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=FIELDS)

        for row in reader:
            writer.writerow(row)
            count += 1

    return count

def get_spot(surf_spots: Path, spot_name: str) -> Surf_Spot:
    with open(surf_spots, mode='r') as file:
        spots_read = csv.DictReader(file)

        for spot in spots_read:
            if spot['name'].lower() == spot_name.lower():
                return Surf_Spot(**spot)
    