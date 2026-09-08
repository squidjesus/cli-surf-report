import pandas as pd
from surf_spot import Surf_Spot

class Report:

    def __init__(self, responses: tuple, surf_spot: Surf_Spot):
        self.atmo_response = responses[0]
        self.marine_response = responses[1]
        self.surf_spot = surf_spot

    def __repr__(self):
        data = []
        for item in self.atmo_response:
            data.append(item)
        for item in self.marine_response:
            data.append(item)
        return("\n".join(item))

    def oneline_report(self):
        pass

    def multiline_report(self):
        pass