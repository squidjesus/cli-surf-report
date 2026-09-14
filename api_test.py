from api_request_func import openmeteo_request
from csv_funcs import get_spot
from report_class import Report
from pathlib import Path

path = Path("demo_surf_spots.csv")

matunuck = get_spot(path, "matunuck")

api_request = openmeteo_request(matunuck)

report = Report(api_request, matunuck)

print(report)


