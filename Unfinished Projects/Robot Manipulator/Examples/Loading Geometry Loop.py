import os
import glob
import random

import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Col import Col
from dash import html
from dash import dcc

from dash.dependencies import Input, Output, State
#from dash_html_components.Br import Br

import dash_vtk
from dash_vtk.utils import to_mesh_state, preset_as_options
import pyvista as pv

import vtk

DATA_PATH = "Assets"



# -----------------------------------------------------------------------------
# GUI setup
# -----------------------------------------------------------------------------

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server

# -----------------------------------------------------------------------------
# Populate scene
# -----------------------------------------------------------------------------

# vehicle geometry
robot_vtk = []
robot_mesh_ids = []
robot_meshes = []

for filename in glob.glob(os.path.join(DATA_PATH, "Assets") + "/*.stl"):
    mesh = pv.read(filename)
    child = dash_vtk.GeometryRepresentation(
        children=[dash_vtk.Mesh(id=f"{part_name}-mesh", state=mesh)],
    )
    robot_vtk.append(child)

    robot_mesh_ids.append(f"{part_name}-mesh")
    robot_meshes.append(mesh)


app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Col(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            dbc.Spinner(color="light"),
                            style={
                                "background-color": "#334c66",
                                "height": "calc(100vh - 230px)",
                                "width": "100%",
                                "text-align": "center",
                                "padding-top": "calc(50vh - 105px)",
                            },
                        ),
                    ],
                    id="vtk-view-container",
                    style={"height": "calc(100vh - 230px)", "width": "100%",},
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server()