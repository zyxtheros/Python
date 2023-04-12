import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import os
import webbrowser

# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

# Build your components for use within the pages
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

pagekeys = ["/", "/Plot", "/Configure"]

#Page containers. contains the elements for each page
page_home = html.Div( [
        html.H1(
            'Welcome to the homepage', 
            style={'textAlign':'center'}

        ),
        html.Button(
            'clicky 1', 
            id='btn-nclicks-1', 
            n_clicks=0
        ),
        dcc.Graph(
            id='bargraph',
            figure=px.bar(
                df, 
                barmode='group', 
                x='Years', 
                y=['Girls Kindergarten', 
                   'Boys Kindergarten']
            )
        )
] )
page_1 = html.Div( [
        html.H1(
            'Grad School in Iran',
            style={'textAlign':'center'}
        ),
        dcc.Graph(
            id='bargraph',
            figure=px.bar(
                df, 
                barmode='group', 
                x='Years', 
                y=['Girls Grade School', 
                   'Boys Grade School']
            )
        )
] )
page_2 = html.Div( [
        html.H1(
            'High School in Iran',
            style={'textAlign':'center'}),
        dcc.Graph(
            id='bargraph',
            figure=px.bar(
                df, 
                barmode='group', 
                x='Years',
                y=['Girls High School', 'Boys High School']
            )
        )
] )
sidebar = html.Div( [
        html.H4("Status Board", className="display-4"),
        html.Hr(),
        html.P(
            "Prototype development dashboard", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href=pagekeys[0], active="exact"),
                dbc.NavLink("Page 1", href=pagekeys[1], active="exact"),
                dbc.NavLink("Page 2", href=pagekeys[2], active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

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
    if pathname == pagekeys[0]: # Home Page Content
        return page_home
    elif pathname == pagekeys[1]:
        return page_1
    elif pathname == pagekeys[2]:
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