from rich.table import Table
from rich.console import Console
from src.report_class import Report

# Compare a spots ideal conditions to the report conditions and color code the data accordingly
# 
# helper func: compare 2 degree values, return a color based on amount of difference
# helper func: convert "N, NE" etc to degrees

# Build the report property by property according to the requested report type.
# Short report sends only a,b,c props to be formatted.
# Detail report sends all.
# Send each property to the appropriate formatting helper funcs (switch case on type of property value)
# Result: string with multiple lines + ascii formatting? or dict for pd.datatable? both?

def data_to_table(reports: list[Report]):
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