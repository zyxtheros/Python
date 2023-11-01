from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
import vtk
import dash_vtk
# Use helper to get a mesh structure that can be passed as-is to a Mesh
from dash_vtk.utils import to_mesh_state
import pyvista as pv

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

# Dash setup
app = Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"width": "100%", "height": "calc(100vh - 15px)"},
    children=[content],
)

if __name__ == "__main__":
    app.run_server()