import sqlite3
import click
from csv_funcs import return_spot_tuples
from pathlib import Path


DEMO_PATH = Path("data/demo_surf_spots.csv")


def load_db() -> sqlite3.Connection:
    connection = sqlite3.connect("data/surf_spots.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS surf_spots (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            location TEXT NOT NULL,
            type TEXT,
            lat REAL NOT NULL,
            long REAL NOT NULL,
            facing TEXT NOT NULL,
            notes TEXT
        )
    """)

    demo_spots = return_spot_tuples(DEMO_PATH)

    cursor.executemany("""
        INSERT OR IGNORE INTO surf_spots (name, location, type, lat, long, facing, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)       
    """, demo_spots)

    connection.commit()

    return connection


def list_spots(connection: sqlite3.Connection, detail: bool):
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * from surf_spots")
    spots = cursor.fetchall()
    for spot in spots:
        if detail == True:
            click.echo(f"{spot['id']}. {spot['location']}: {spot['name']} | Break Type: {spot['type']} | Facing: {spot['facing']} | Notes: {spot['notes']}")
        else:
            click.echo(f"{spot['id']}. {spot['location']}: {spot['name']}")

def add_spot(connection: sqlite3.Connection):
    cursor = connection.cursor()
    new_spot = {
        'name'  : click.prompt("Surf Spot name - must be unique"),
        'location': click.prompt("Location (general location, ie: 'Newport, RI' or 'El Sunzal, ES')"),
        'type'  : click.prompt("Break type (reef, point, beach etc.)"),
        'lat'   : click.prompt("Latitude (to 4 dec places '1.1234')"),
        'long'  : click.prompt("Longitude (to 4 dec places '-1.1234')"),
        'facing': click.prompt("Direction the spot is facing in letters, ie: 'S' or 'SSW' or 'NE' etc."),
        'notes' : click.prompt("Notes (optional)")
    }
    spot = tuple(new_spot.values())
    cursor.execute("""
        INSERT OR IGNORE INTO surf_spots (name, location, type, lat, long, facing, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, spot)
    connection.commit()
    click.echo(f"Added surf spot: {new_spot['name']}")


def rm_spot(connection: sqlite3.Connection, name: str):
    pass
