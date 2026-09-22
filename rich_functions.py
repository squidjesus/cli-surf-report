import time
import sqlite3
from rich.table import Table
from rich.console import Console
from rich.progress import track
from report_class import Report
from database_functions import get_spot
from api_request import openmeteo_request


def get_reports(spots: list[str], db: sqlite3.Connection) -> list[Report]:
    reports = []
    num_spots = len(spots)
    for s in track(spots, description=f"Requesting data from OpenMeteo api for {num_spots} spots...", transient=True):
        spot = get_spot(db, s)
        if spot == None:
            continue
        api_req = openmeteo_request(spot)
        report = Report(api_req, spot)
        reports.append(report)
    return reports


def print_table(reports: list[Report]):
    dicts = []
    for r in reports:
        dicts.append(r.current_report())
    table = Table(title="Current Conditions Report")
    for key in dicts[0].keys():
        table.add_column(key, justify="center")
    for report in dicts:
        table.add_row(*[str(value) for value in report.values()], end_section=True)

    console = Console()
    console.print(table)
