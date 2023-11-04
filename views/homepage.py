
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
                            persistence_type = 'local',
                            clearable = False,
                            options = [
                                {'label': 'Protetor solar Natura FPS 50 - Pele normal a oleosa', 'value': 'protetor'},
                                {'label': 'Garmin Forerunner 245', 'value': 'forerunner 245'},
                                {'label': 'Garmin Forerunner 255s', 'value': 'forerunner 255s'}
                            ],
                            value = 'Protetor solar Natura FPS 50 pele normal a oleosa'
                        )
                    ], className = 'selecionar-produto')
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Label('Período disponível: 01/10/2023 → hoje', id = 'label-periodo')
                ]),
                dbc.Row([
                    html.Div([
                        dbc.Input(
                            id="my-date-picker-range",
                            placeholder = "dd-mm-yyyy", 
                            value = "01-10-2023", 
                            persistence = True,
                            type = "day", 
                            required = "required",  
                            min = "01-10-2023", 
                            max = "31-10-2023"
                        ),
                        DashIconify(icon="ic:round-arrow-right-alt",
                            color = '#666666',
                            width = 30,
                            id ="arrowDate"
                        ),
                        dbc.Input(
                            id="my-date-picker-range2", 
                            type="day",
                            value="31-10-2023", 
                            persistence=True, 
                            required = "required",  
                            min="01-10-2023", 
                            max = "31-10-2023"
                        )
                    ], id = 'datePicker')
                ])
            ]),
            dbc.Col([
                html.A(
                    html.Img(
                        src="/assets/protetor_foto_sem_fundo.png",
                        height="200px"
                    ),
                    href = 'https://www.natura.com.br/p/protetor-facial-gel-creme-fps-60-fpuva-20-fotoequilibrio-50-g/103144?listTitle=category%20page%20list%20showcase%20-%20rosto%20-%20protecao%20solar&position=2'
                )
                
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








