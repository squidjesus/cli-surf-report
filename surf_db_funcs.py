import sqlite3
import click
from demo import load_demo_spots


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

    # Prompts to add spots if database is empty
    cursor.execute("SELECT * FROM surf_spots LIMIT 1")
    spots = cursor.fetchone()
    if not spots:
        click.echo('Surf spots database is empty.')
        choice = click.prompt("1. Load demo spots\n2. Add a spot\n3. Exit\n", type=click.Choice(["1","2","3"]))
        match choice:
            case "1":
                load_demo_spots(connection)
            case "2":
                add_spot(connection)

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
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM surf_spots WHERE name LIKE ?
    COLLATE NOCASE
    """, (name,))

    spot = cursor.fetchone()
    if spot is None:
        click.secho(f"{name} did not match any spots in the database", fg='red')
        exit(1)

    if click.confirm(f'Delete surf spot {spot[1]}?'):
        cursor.execute("DELETE FROM surf_spots WHERE id = ?", (spot[0],))
        connection.commit()
        click.echo(f"Deleted {name}")
        exit(0)

    click.echo("Delete cancelled")
    exit(0)    
