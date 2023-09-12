#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output

#######################################################################
# APP
#######################################################################

app = Dash(
    __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    update_title = "Atualizando ...",
    # suppress_callback_exceptions = True
)

app.title = "Monitoramento de Preços"
server = app.server