#robot arm modules
import multiprocessing
import pyvista as pv
from pyvista import themes
import os
from sys import exit # used to kill the program
# dash webpaeg modules
import websocket
from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
import vtk
import dash_vtk
from dash_vtk.utils import to_mesh_state
from dash_vtk.utils import presets
import dash_daq as daq
import os
import webbrowser

# set up the websocket connection
ws = websocket.WebSocket()
address = "ws://192.168.4.1/"
#try:
#    ws.connect(address)
#except:
#    print("Error: address "+address+" failed to connect")


# Build the web app
app = Dash(__name__)

root = "Assets/"
file = "J0"
fileType = ".stl"
mesh = pv.read(root+file+fileType)
mesh_state = to_mesh_state(mesh)

content = dash_vtk.View([
    dash_vtk.GeometryRepresentation([
        dash_vtk.Mesh(state=mesh_state)
    ]),
])

if __name__ == "__main__":
    app.run_server()

app.layout = html.Div([
    html.H1('Robot Arm Controller'),
    dbc.Row([
        dbc.Col([
            daq.Knob(id='servo-knob', max = 180, value = 90, scale = {'interval':15}),
            html.Div(id='knob-result')   
        ]),
        dbc.Col([
            html.Div(
                style={"width": "50%", "height": "calc(100vh - 15px)"},
                children=[content],
            )
        ]),
    ])
])



@app.callback(Output('knob-result', 'children'), Input('servo-knob', 'value')) # Setup the callback for updating data
def update_output(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"



# Run the web app
PORT = 1100
def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(PORT))

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", port=PORT)


if __name__=='__main__':
    main()