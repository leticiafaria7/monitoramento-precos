
################################################################################
# BIBLIOTECAS
################################################################################

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from flask_login import logout_user, current_user
from views import homepage
from callbacks import callbacks_gerais
from app import app
import dash_bootstrap_components as dbc

pd.options.mode.chained_assignment = None

################################################################################
# LAYOUT
################################################################################

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            html.Div(id = "page-content"),
            html.Div([
                dbc.RadioItems(
                    persistence=True,
                    persistence_type = "local",
                    id="produtos",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options = [
                        {'label': 'Protetor solar Natura FPS 50 - Pele normal a oleosa', 'value': 'protetor'},
                        {'label': 'Garmin Forerunner 245', 'value': 'forerunner 245'},
                        {'label': 'Garmin Forerunner 255s', 'value': 'forerunner 255s'}
                    ],
                    value = 'Protetor solar Natura FPS 50 pele normal a oleosa'
                )
            ], hidden=True) 
        ], md=12, style={'background-color':'transparent', 'height':'1080px'})
    ])
], fluid = True) # o conteúdo se espalha ao longo da tela

@app.callback(
        Output('page-content', 'children'), 
        [Input('url', 'pathname')]
)

def render_page(pathname):
    if pathname == '/' or pathname == '/homepage':
        return homepage.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)

