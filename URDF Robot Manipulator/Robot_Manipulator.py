
from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
import vtk
import dash_vtk
# Use helper to get a mesh structure that can be passed as-is to a Mesh
from dash_vtk.utils import to_mesh_state, presets
import pyvista as pv
import dash_daq as daq
import os
import webbrowser
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
# Setup the over-arching page components
# -----------------------------------------------------------------------------    
robotViewer = dash_vtk.View(
    background = [34/255, 34/255, 34/255],
    children = [ # add the previously parsed VTK geometry to the viewe
        geometry[0],
        geometry[1],
    ], 
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
        ])
    ])
])

# -----------------------------------------------------------------------------
# Define the callbacks for components with outputs
# ----------------------------------------------------------------------------- 
@app.callback(Output('knob-result1', 'children'), Input('servo-knob1', 'value')) # callback for updating data via knob interaction
def update_knob1(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"
@app.callback(Output('knob-result2', 'children'), Input('servo-knob2', 'value')) # callback for updating data via knob interaction
def update_knob2(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"
@app.callback(Output('knob-result3', 'children'), Input('servo-knob3', 'value')) # callback for updating data via knob interaction
def update_knob(value):
    #ws.send(f'SERVO:{value},23') # send the command over websocket
    print(f'Servo angle: {value}'+u"\N{DEGREE SIGN}")
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"
def toDropOption(name):
    return {"label": name, "value": name}

app.layout = dbc.Container([
    html.H1('Robot Arm Controller'),
    dbc.Row([
        dbc.Col([
           arm_controller,
            # upload for elems
            dcc.Upload(
                #id=f'{APP_ID}_elems_upload',
                multiple=False,
                children=[
                    dbc.Label('Upload Element Mesh'),
                    dbc.Button('Upload Elements', color='primary')
                ]
            ),
            html.H3('Step 2: Upload Your Element Results'),
            # upload for elem data
            dcc.Upload(
                multiple=False,
                children=[
                        dbc.Label('Upload Element Results Data'),
                        dbc.Button('Upload Results', color='primary')
                ]
            ),
            html.H3('Step 3: Play with colors!'),
            dbc.Label('Color Map'),
            dcc.Dropdown(
                options=list(map(toDropOption, presets)),
                value="erdc_rainbow_bright",
            ),
            dbc.Label('Cell Value Threshold'),
            dcc.RangeSlider(
                min=0.,
                max=1.,
                step=.01,
                value=[0., 1.],
                marks={
                    0.: '0%',
                    .25: '25%',
                    .50: '50%',
                    .75: '75%',
                    1.0: '100%'
                },
            ),
            dbc.FormText('% of maximum value in data set'),
            dbc.Checklist(
                options=[
                    {"label": "Show Element Edges", "value": 1}
                ],
                switch=True,
                value=[1]
            )
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