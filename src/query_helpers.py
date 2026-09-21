import sqlite3
import click


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
    