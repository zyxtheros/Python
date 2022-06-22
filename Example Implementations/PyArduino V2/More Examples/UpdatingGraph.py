import dash
from dash.dependencies import Output, Input
from dash import dcc, html
import plotly
import random
import plotly.graph_objs as go
from collections import deque # allows for creating an array with a constant size that we can update to
import os
import webbrowser

X = deque(maxlen=20) # array of x coordinates
Y = deque(maxlen=20) # array of y coordinates

X.append(1) # start off with initial set to 1 for x and y
Y.append(1)


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True), # this is the actual graph element
        dcc.Interval(
            id='graph-update',  # what we are updating
            interval=1000,      # How fast the interval will occur
            n_intervals = 0
        ),
    ]
)

@app.callback(  
                Output('live-graph', 'figure'), # output() parameters: ID of the element, type of element with that ID
                [Input('graph-update', 'n_intervals')] # create an input 'event' of type interval (n_intervals) with ID graphupdate
              )
def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
        )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}

# Run app
PORT = 1100
def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(PORT))

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", port=PORT)

if __name__=='__main__':
    main()
