# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Event, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
data_path = 'data/example_data.csv'

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app_colors = {
    'background': '#0C0F0A',
    'text': '#FFFFFF',
    'sentiment-plot':'#41EAD4',
    'volume-bar':'#FBFC74',
    'someothercolor':'#FF206E',
}

app.layout = html.Div(children=[
    html.H1(children='Regeneron AI'),
    html.H5(children='''
        Empowering building owners to be energy smart, more efficient, and provide real cost savings.
    '''),

    html.Label('My Buildings', id='init-dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Roble Hall', 'value': 'Roble'},
            {'label': 'Branner Hall', 'value': 'Branner'},
            {'label': 'Lagunita Court', 'value': 'Lag'}
        ],
        value=['Roble'],  style={'width':'65%','margin-left':10,'margin-right':10,'max-width':50000}
    ),

    # Dashboard div
    html.Div(children=[
        html.Div(children=[
            html.Label('Summary'),
            dcc.Markdown(children='''
                * Total Electric Usage     1465 kWh
                * Total Electric Bill      $1283.21

                * Total Water Usage        Blah
                * Total Water Bill         Blah
            '''),

            html.Label('Appliances'),
            # generate_app_table(),
        ])

    ], id='dashboard-main'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

def generate_summary_table():
    return html.Table(
        html.Tr([])
    )

if __name__ == '__main__':
    app.run_server(debug=True)
