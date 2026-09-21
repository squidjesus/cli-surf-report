from src.api_request import openmeteo_request
from src.surf_db_funcs import get_spot
from src.report_class import Report
from src.config import DB_PATH
from src.report_funcs import print_current_reports
import sqlite3

connection = sqlite3.connect(DB_PATH)

sunzal = get_spot(connection, "El Sunzal Point")
matunuck = get_spot(connection, "Matunuck")

request1 = openmeteo_request(sunzal)
request2 = openmeteo_request(matunuck)

reports = [
    Report(request1, sunzal),
    Report(request2, matunuck)
]

#print(report)

print_current_reports(reports)


