from api_request_func import openmeteo_request
from surf_db_funcs import get_spot
from report_class import Report
import sqlite3

connection = sqlite3.connect("../data/surf_spots.db")

matunuck = get_spot(connection, "matunuck")

api_request = openmeteo_request(matunuck)

report = Report(api_request, matunuck)

print(report)


