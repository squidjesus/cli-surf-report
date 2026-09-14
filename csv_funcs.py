import csv
import click
from pathlib import Path
from surf_spot_class import Surf_Spot

# Fields in a valid "Surf Spots.csv"
FIELDS = ['name', 'location', 'type', 'lat', 'long', 'facing', 'notes']

# Create "surf_spots.csv" in the root folder with the appropriate field names
def create_spot_file(surf_spots: Path):
    with open(surf_spots, mode="w", newline="") as file:
        spots_writer = csv.DictWriter(file, fieldnames=FIELDS)
        spots_writer.writeheader()
    return


# Check a surf spots CSV contains the correct fields
def validate_spots_csv(surf_spots: Path) -> bool:
    with open(surf_spots, mode='r') as file:
        spots_read = csv.DictReader(file)
        if spots_read.fieldnames != FIELDS:
            return False
        return True


def return_spot_tuples(spots_csv: Path) -> list[tuple]:
    tuples = []
    with open(spots_csv, mode='r') as file:
        spots_read = csv.DictReader(file)
        for spot in spots_read:
            try:
                tuples.append(
                    (
                        spot['name'],
                        spot['location'],
                        spot['type'],
                        spot['lat'],
                        spot['long'],
                        spot['facing'],
                        spot['notes']
                    )
                )
            except:
                raise Exception("Invalid field name in spots CSV")
    
    return tuples