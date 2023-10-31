
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

# pd.options.mode.chained_assignment = None

################################################################################
# LAYOUT
################################################################################

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        html.H3('Monitoramento de preços', className = 'text-primary', id = 'titulo')
    ], className = 'jumbotron')
])







# dbc.Col([
#     dbc.Row([
#         html.H1('Monitoramento de preços', className = 'text-primary')
#     ])
# ])










