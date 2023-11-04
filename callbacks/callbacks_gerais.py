
################################################################################
# BIBLIOTECAS
################################################################################

from app import app
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from flask_login import current_user
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_iconify import DashIconify
import numpy as np

################################################################################
# BASES DE DADOS
################################################################################

# protetor natura
protetor_natura = pd.read_excel('assets/protetor_natura.xlsx', engine = 'openpyxl')
protetor_natura = protetor_natura.groupby(['data'])['preco'].mean().to_frame().reset_index()

# forerunner 255s
forerunner_255s = pd.read_excel('assets/forerunner_255s.xlsx', engine = 'openpyxl')
forerunner_255s['site_cor'] = forerunner_255s['site'] + " - " + forerunner_255s['cor']
forerunner_255s = forerunner_255s.groupby(['data', 'site_cor'])['preco'].mean().to_frame().reset_index()
forerunner_255s = forerunner_255s[forerunner_255s['preco'] != 0]

# forerunner 245
forerunner_245 = pd.read_excel('assets/forerunner_245.xlsx', engine = 'openpyxl')
forerunner_245['site_cor'] = forerunner_245['site'] + " - " + forerunner_245['cor']
forerunner_245 = forerunner_245[~forerunner_245['hora'].isna()]
forerunner_245 = forerunner_245.groupby(['data', 'site_cor'])['preco'].mean().to_frame().reset_index()
forerunner_245['preco_medio'] = round(forerunner_245['preco'].mean(), 2)

################################################################################
# GRÁFICO
################################################################################

@app.callback(
    Output('variacao-preco', 'figure'),

    Input('produtos', 'value'),
    # Input('my-date-picker-range', 'value'),
    # Input('my-date-picker-range2', 'value'),
    prevent_inicial_call = True
)

def grafico_variacao_preco(
    produto
    # start_date, 
    # end_date
):

    base_dados = None

    if produto == "Protetor solar Natura FPS 50 - Pele normal a oleosa":
        base_dados = protetor_natura
    
    if produto == "Garmin Forerunner 245":
        base_dados = forerunner_255s

    if produto == "Garmin Forerunner 245":
        base_dados = forerunner_245

    if base_dados is not None:

        df = base_dados

        fig = px.line(
            x = df['data'],
            y = df['preco'],
            width = 1200,
            height = 600
            # title = produto,
            # color_discrete_sequence = ['#c74458', '#76a6f1', '#618e8c', '#df8c37']
        )
        
        fig.update_layout(
                plot_bgcolor = 'rgba(0,0,0,0)',
                paper_bgcolor = 'rgba(0,0,0,0)',
                xaxis = dict(
                    tickfont = dict(
                        family = 'Ubuntu',
                        size = 12   ,
                        color = 'rgb(82, 82, 82)'                             
                    )
                ),
                yaxis = dict(
                    tickfont = dict(
                        family = 'Ubuntu',
                        size = 10,
                        color = 'rgb(82, 82, 82)'
                    ),
                ),
                legend_title_text = 'Site / cor',
                yaxis_tickformat = ".2f",
                xaxis_gridcolor = '#e4e4e4',
                yaxis_gridcolor = '#e4e4e4'      
            )
        
        fig.update_traces(line = dict(width = 4))
        fig.update_xaxes(title_text = None, title_font = dict(size=16, family='Ubuntu'))
        fig.update_yaxes(title_text = 'Preço', title_font = dict(size=16, family='Ubuntu'), rangemode = "tozero")
    
    else:
        fig = go.Figure()
    
    return fig





