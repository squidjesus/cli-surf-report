import sqlite3
import click
import csv
from pathlib import Path


def get_by_name(connection: sqlite3.Connection, name: str):
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM surf_spots WHERE name LIKE ?
    COLLATE NOCASE
    """, (name,))

    spot = cursor.fetchone()
    if spot is None:
        click.secho(f"{name} did not match any spots in the database", fg='red')
        return

    return spot


def del_by_id(connection: sqlite3.Connection, id: int):
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM surf_spots WHERE id = ?", (id,))
        connection.commit()
    except:
        click.secho(f"Spot with id: {id} not found, could not delete", fg="red")
        exit(1)
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