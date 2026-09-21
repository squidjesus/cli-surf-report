import sqlite3
import click
from src.csv_funcs import return_spot_tuples
from src.config import DEMO_PATH


def load_demo_spots(connection: sqlite3.Connection):
    cursor = connection.cursor()
    query = "INSERT OR IGNORE INTO surf_spots (name, location, type, lat, long, facing, notes) VALUES (?, ?, ?, ?, ?, ?, ?)"
    tuples = return_spot_tuples(DEMO_PATH)
    for tuple in tuples:
        cursor.execute(query, tuple)
    connection.commit()
    click.echo("Demo spots loaded")

def run_demo():
    pass
