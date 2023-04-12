import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import os
import webbrowser
from pages import * # Include the custom pages file



# Build your components for use within the pages
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div( [
    dcc.Location(id="url"),
    sidebar,
    content
] )


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == extensions[0]: # Home Page Content
        return page_home
    elif pathname == extensions[1]:
        return page_1
    elif pathname == extensions[2]:
        return page_2
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

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