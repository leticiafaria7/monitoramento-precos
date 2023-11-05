
################################################################################
# BIBLIOTECAS
################################################################################

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from flask_login import logout_user, current_user
from app import app
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

# pd.options.mode.chained_assignment = None

################################################################################
# LAYOUT
################################################################################

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        html.H3('Monitoramento de preços', id = 'titulo'),
        html.Hr(),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Label('Produto', id = 'label-produto')
                ]),
                dbc.Row([
                    html.Div([
                        dcc.Dropdown(
                            id = 'produtos',
                            # persistence = True,
                            persistence_type = 'session',
                            clearable = False,
                            options = [
                                {'label': 'Protetor solar Natura FPS 50 - Pele normal a oleosa', 'value': 'Protetor solar Natura FPS 50 - Pele normal a oleosa'},
                                {'label': 'Garmin Forerunner 245', 'value': 'Garmin Forerunner 245'},
                                {'label': 'Garmin Forerunner 255s', 'value': 'Garmin Forerunner 255s'}
                            ],
                            value = 'Protetor solar Natura FPS 50 - Pele normal a oleosa'
                        )
                    ], className = 'selecionar-produto')
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Label('Selecionar período:', id = 'label-periodo')
                ]),
                dbc.Row([
                    html.Div([
                        dbc.Input(
                            id="my-date-picker-range",
                            placeholder = "dd-mm-yyyy", 
                            value = "2023-10-01", 
                            persistence = True,
                            type = "date", 
                            required = "required",  
                            min = "2023-10-01", 
                            max = "2023-11-01"
                        ),
                        DashIconify(icon="ic:round-arrow-right-alt",
                            color = '#666666',
                            width = 30,
                            id ="arrowDate"
                        ),
                        dbc.Input(
                            id="my-date-picker-range",
                            placeholder = "dd-mm-yyyy", 
                            value = "2023-11-01", 
                            persistence = True,
                            type = "date", 
                            required = "required",  
                            min = "2023-10-01", 
                            max = "2023-11-01"
                        )
                    ], id = 'datePicker')
                ])
            ]),
            dbc.Col([
                html.Div(id = 'imagem')
            ])
        ]),
        dbc.Row([
            html.Div([
                dcc.Graph(
                    id = 'variacao-preco',
                    config = {'displayModeBar': False}
                )
            ], id = "grafico")
        ])
    ], className = 'jumbotron')
])








