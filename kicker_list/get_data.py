import pandas as pd
import numpy as np
import plotly.graph_objs as go

def get_data():
    
    kicker_scores = pd.Series({'Day':[1,2,3,4,5,6,7,8],
                    'Gidi':[20,22,29,40,42,49,61,90],
                     'Firas':[10,12,21,30,43,41,51,50]})
    
    gidiplot = go.Scatter(
          x = kicker_scores.Day,
          y = kicker_scores.Gidi,
          mode = 'lines',
          name = 'Gidi'
          )
    
    firasplot = go.Scatter(
          x = kicker_scores.Day,
          y = kicker_scores.Firas,
          mode = 'lines',
          name = 'Firas'
          )
    
    
    out = {'firstvalue':13,
           'secondvalue':'Gidi',
           'listekiste':[13, 154,26, 23, 15, 16, 56, 53, 42],
           'kickerscores':kicker_scores,
           'kickerplot':gidiplot}
    
    return out