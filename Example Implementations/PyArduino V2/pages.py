import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

extensions = ["/", "/Plot", "/Configure"]

# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
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
SIDEBAR_STYLE = { # styling the sidebar
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    # "background-color": "#f8f9fa",
}
sidebar = html.Div( [
        html.H4("Status Board", className="display-4"),
        html.Hr(),
        html.P(
            "Prototype development dashboard", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Not Home", href=extensions[0], active="exact"),
                dbc.NavLink(extensions[1].lstrip("/"), href=extensions[1], active="exact"),
                dbc.NavLink(extensions[2].lstrip("/"), href=extensions[2], active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)




