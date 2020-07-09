import plotly
import plotly.graph_objs as go
import json
from app import mongoConn
st_shp = mongoConn.db.st_shp


def create_plot(state):
      for i in st_shp.find({'State':state}):
            y = i['Latitude']
            x = i['Longitude']

      fig = go.Figure()
      fig.add_trace(go.Scatter(x = x , y=y, mode = 'lines' , hoverinfo = 'none' , line = dict(color='rgb(0,0,0)')))
      fig.update_layout(height = 1000 , width = 1500 , plot_bgcolor='white', xaxis = dict(showline=False , showgrid = False, showticklabels=False) 
                        , yaxis = dict(showline=False,showgrid = False, showticklabels=False))

      graphJSON = json.dumps(fig , cls = plotly.utils.PlotlyJSONEncoder)
      return graphJSON
