import csv
from pathlib import Path

FIELDS = ['name','type','lat','long','opt_swells','opt_wind','opt_tide','notes']

def create_spot_file(surf_spots: Path):
    with open(surf_spots, mode="w", newline="") as file:
        spots_writer = csv.DictWriter(file, fieldnames=FIELDS)
        spots_writer.writeheader()

def list_spots(surf_spots: Path) -> list :
    spots = []
    with open(surf_spots, mode='r') as file:
        spots_read = csv.DictReader(file)        
        for spot in spots_read:
            spots.append(f"Name: {spot['name']}, Lat: {spot['lat']}, Long: {spot['long']}") 
        return spots

def add_spot(surf_spots: Path, new_spot: dict):
    with open(surf_spots, mode='a', newline='') as file:
        spots_write = csv.DictWriter(file, fieldnames=FIELDS)
        spots_write.writerow(new_spot)
    return

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

    

    