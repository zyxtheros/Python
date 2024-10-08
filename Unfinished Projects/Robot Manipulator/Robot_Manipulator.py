
from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
#import vtk
import dash_vtk
# Use helper to get a mesh structure that can be passed as-is to a Mesh
from dash_vtk.utils import to_mesh_state, presets
#import pyvista as pv
import dash_daq as daq
import os
import webbrowser
import json
# Custom Python modules
from helper import *


# color pallette from Darkly theme (DBC)
darkly_theme = get_css_theme("assets/style.css")
daq_theme = {       # provides theme parameters to use for all daq components. Additional parameters must be specified in assets/style.css
    'dark'      :   False,
    'detail'    :   darkly_theme['success'],
    'primary'   :   darkly_theme['primary'],
    'secondary' :   darkly_theme['secondary']
}

# -----------------------------------------------------------------------------
# GUI setup
# -----------------------------------------------------------------------------
app = Dash(__name__, external_stylesheets = [dbc.themes.DARKLY])    # Dash setup
server = app.server

# -----------------------------------------------------------------------------
# Populate the 3D view screen
# -----------------------------------------------------------------------------
J0 = model("J0", color = RGB["BLUE"])
J1 = model("J1", color = RGB["RED"])
geometry = get_model_geometry()

# -----------------------------------------------------------------------------
# Define the callbacks for components with outputs
# ----------------------------------------------------------------------------- 
@app.callback(Output('knob-result1', 'children'), Input('servo-knob1', 'value')) # callback for updating data via knob interaction
def update_knob1(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    #print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"

@app.callback(Output('knob-result2', 'children'), Input('servo-knob2', 'value')) # callback for updating data via knob interaction
def update_knob2(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    #print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"

@app.callback(Output('knob-result3', 'children'), Input('servo-knob3', 'value')) # callback for updating data via knob interaction
def update_knob(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    #print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"

@app.callback(
    Output('click-info-output', 'children'),
    Input('click-info-view', 'clickInfo')
)
def display_clicked_content(click_info):
    return json.dumps(click_info, indent=2)

def toDropOption(name):
    return {"label": name, "value": name}

# -----------------------------------------------------------------------------
# Setup the over-arching page components
# -----------------------------------------------------------------------------    
robotViewer = dash_vtk.View(
    background = [34/255, 34/255, 34/255],
    children = geometry, # add the previously parsed VTK geometry to the viewer    
)

arm_controller = dbc.Card([
    dbc.Row([
        dbc.Col([
            html.H3('Axis 1'),
            daq.Knob(
                id='servo-knob1', 
                max = 180, 
                value = 90, 
                scale = {'interval':15},
                color = daq_theme['detail']
            ),
            html.Div(id='knob-result1')  # set the ID that will be returned from the callback
        ]),
        dbc.Col([
            html.H3('Axis 2'),
            daq.Knob(
                id='servo-knob2', 
                max = 180, 
                value = 90, 
                scale = {'interval':15},
            ),
            html.Div(id='knob-result2'), # set the ID that will be returned from the callback
        ]),
        dbc.Col([
            html.H3('Axis 2'),
            daq.Knob(
                id='servo-knob3', 
                max = 180, 
                value = 90, 
                scale = {'interval':15},
            ),
            html.Div(id='knob-result3'), # set the ID that will be returned from the callback
        ]),
    ]),
    dbc.Row([
        html.Div(
            id="click-info-output",
            style={'overflowX': 'scroll'}
        )
    ])
])

app.layout = dbc.Container([
    html.H1('Robot Arm Controller'),
    dbc.Row([
        dbc.Col([
           arm_controller,
        ],
            width=4
        ),
        dbc.Col([
            html.Div(
                html.Div(
                    style={"width": "100%", "height": "100%"},
                    children = robotViewer
                ),
                style={"height": "100%"},
            ),
        ]),

    ]),
],
    fluid=True,
    style={"height": "75vh"},
)


# Run the web app
PORT = 8050
def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(PORT))

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", port=PORT)

if __name__=='__main__':
    main()