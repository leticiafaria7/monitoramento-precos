
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

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id = "page-content")
])



# dbc.Container(children=[
#     dbc.Row([
#         dbc.Col([
#             dcc.Location(id='url'),
#             html.Div(id = "page-content"),
#         ], md=12, style={'background-color':'transparent', 'height':'1080px'})
#     ])
# ], fluid = True) # o conteúdo se espalha ao longo da tela

@app.callback(
        Output('page-content', 'children'), 
        [Input('url', 'pathname')]
)

def render_page(pathname):
    if pathname == '/' or pathname == '/homepage':
        return homepage.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)

