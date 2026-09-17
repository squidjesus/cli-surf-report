import pandas as pd
import click
from report_class import Report

# Compare a spots ideal conditions to the report conditions and color code the data accordingly
# 
# helper func: compare 2 degree values, return a color based on amount of difference
# helper func: convert "N, NE" etc to degrees

# Build the report property by property according to the requested report type.
# Short report sends only a,b,c props to be formatted.
# Detail report sends all.
# Send each property to the appropriate formatting helper funcs (switch case on type of property value)
# Result: string with multiple lines + ascii formatting? or dict for pd.datatable? both?

def print_current_reports(reports: list[Report]):
    pd.set_option('display.colheader_justify', 'center')
    #data = []
    #for report in reports:
    #    spot_report = report.current_report()
    #    data.append(spot_report)
    df = pd.DataFrame.from_records([r.current_report() for r in reports])
    click.echo(df.to_string(index=False))