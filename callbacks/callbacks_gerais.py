
#####################################################################################################################################
# BIBLIOTECAS
#####################################################################################################################################

from app import app
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from flask_login import current_user
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_iconify import DashIconify
import numpy as np
from dash import Dash, dcc, html

#####################################################################################################################################
# BASES DE DADOS
#####################################################################################################################################

# protetor natura
protetor_natura = pd.read_excel('assets/protetor_natura.xlsx', engine = 'openpyxl')
protetor_natura = protetor_natura.groupby(['data'])['preco'].mean().to_frame().reset_index()
protetor_natura['preco_medio'] = round(protetor_natura['preco'].mean(), 2)
protetor_natura['site_cor'] = 'natura'

# forerunner 255s
forerunner_255s = pd.read_excel('assets/forerunner_255s.xlsx', engine = 'openpyxl')
forerunner_255s['site_cor'] = forerunner_255s['site'] + " - " + forerunner_255s['cor']
forerunner_255s = forerunner_255s[forerunner_255s['cor'] == 'preto']
forerunner_255s = forerunner_255s.groupby(['data', 'site_cor'])['preco'].mean().to_frame().reset_index()
forerunner_255s = forerunner_255s[forerunner_255s['preco'] != 0]
# forerunner_255s['preco_medio'] = round(forerunner_255s.groupby('site')['preco'].transform('mean'), 2)
forerunner_255s['preco_medio'] = round(forerunner_255s['preco'].mean(), 2)

# forerunner 245
forerunner_245 = pd.read_excel('assets/forerunner_245.xlsx', engine = 'openpyxl')
forerunner_245['site_cor'] = forerunner_245['site'] + " - " + forerunner_245['cor']
forerunner_245 = forerunner_245[~forerunner_245['hora'].isna()]
forerunner_245 = forerunner_245.groupby(['data', 'site_cor'])['preco'].mean().to_frame().reset_index()
forerunner_245['preco_medio'] = round(forerunner_245['preco'].mean(), 2)

#####################################################################################################################################
# GRÁFICO
#####################################################################################################################################

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
    
    if produto == "Garmin Forerunner 255s":
        base_dados = forerunner_255s

    if produto == "Garmin Forerunner 245":
        base_dados = forerunner_245

    if base_dados is not None:

        df = base_dados

        fig = px.line(
            x = df['data'],
            y = df['preco'],
            color = df['site_cor'],
            width = 1200,
            height = 400,
            color_discrete_sequence = ['#3860A5', '#C74458']
            # title = produto
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
                xaxis_gridcolor = '#eeeeee',
                yaxis_gridcolor = '#eeeeee'      
            )
        
        fig.update_traces(line = dict(width = 4))
        fig.update_xaxes(title_text = None, title_font = dict(size=16, family='Ubuntu'))
        fig.update_yaxes(title_text = 'Preço', title_font = dict(size=13, family='Ubuntu'), rangemode = "tozero")
        fig.add_trace(px.line(df, 
                              x='data', 
                              y='preco_medio',
                              color_discrete_sequence = ['#b4b4b4'],
                              line_dash_sequence = ['dash']).data[0])
    
    else:
        fig = go.Figure()
    
    return fig


#####################################################################################################################################
# IMAGEM
#####################################################################################################################################

@app.callback(
    Output('imagem', 'children'),
    Input('produtos', 'value')
)

def mudar_imagem(produto):

    if produto == "Protetor solar Natura FPS 50 - Pele normal a oleosa":
        
        imagem_ = html.A(
            html.Img(
                src = 'assets/protetor_foto_sem_fundo.png',
                height = '200px',
            ), href = 'https://www.natura.com.br/p/protetor-facial-gel-creme-fps-60-fpuva-20-fotoequilibrio-50-g/103144?listTitle=category%20page%20list%20showcase%20-%20rosto%20-%20protecao%20solar&position=2'
        )
    
    if produto == "Garmin Forerunner 245":
        imagem_ = html.A(
            html.Img(
                src = 'assets/forerunner_245_sem_fundo.png',
                height = '200px',
            ), href = 'https://www.amazon.com.br/Garmin-Forerunner%C2%AE-Music-smartwatch-corrida/dp/B09WTJ48NB'
        )


    if produto == "Garmin Forerunner 255s":
        imagem_ = html.A(
            html.Img(
                src = 'assets/forerunner_255s_sem_fundo.png',
                height = '200px',
            ), href = 'https://www.amazon.com.br/Esportivo-Garmin-Forerunner-Vermelho-Card%C3%ADaco/dp/B07RG5VCFT/ref=d_pd_vtp_sccl_2_3/133-9424469-2772417?pd_rd_w=NFm5C&content-id=amzn1.sym.38f285bf-51cf-4756-b852-81b03b491f92&pf_rd_p=38f285bf-51cf-4756-b852-81b03b491f92&pf_rd_r=Z1M3R65AM1N4RC825E3M&pd_rd_wg=SJiM7&pd_rd_r=956eaa46-c16e-4301-9074-bafe2aa70cc1&pd_rd_i=B07RG5VCFT&th=1'
        )

    return imagem_
