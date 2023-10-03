
##################################################################################################################################################################
# bibliotecas
##################################################################################################################################################################

import pandas as pd
import datetime
import re

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

##################################################################################################################################################################
# parte do selenium
##################################################################################################################################################################

options_ = Options()
options_.add_argument('--headless') # faz toda a rotina, mas o navegador não abre
options_.add_argument('window-size=1500,800') # define o tamanho da tela

navegador = webdriver.Chrome(options = options_)
navegador.get('https://www.natura.com.br/p/protetor-facial-gel-creme-fps-60-fpuva-20-fotoequilibrio-50-g/103144?listTitle=category%20page%20list%20showcase%20-%20rosto%20-%20protecao%20solar&position=2')

sleep(2)

# converter em objeto beautifulsoap
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# criar uma lista vazia para colocar os dados printados depois
monitoramento_preco = []

# pegar o preço no site
precos = site.find_all('h6', class_=lambda x: x and re.compile(r'^MuiTypography-root natds').search(x))

for preco in precos:
    if "R$" in preco.text:
        reais = preco.text
        break

# arrumar o preco
reais = reais.replace("R$", "")
reais = reais.replace(",", ".")
reais = reais.strip()

# salvar a data e a hora atual em variáveis
data = datetime.date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().time().strftime("%H:%M")

# fazer o append na lista
monitoramento_preco.append([data,
                            hora,
                            reais,
                            'natura'])

# colocar em um dataframe
df = pd.DataFrame(monitoramento_preco, columns = ['data', 'hora', 'preco', 'site'])
df['preco'] = df['preco'].astype('float')

# chamar a base já existente e concatenar o novo preço
base = pd.read_excel('assets/protetor_natura.xlsx', 'protetor_natura', engine = 'openpyxl')
df = pd.concat([base, df])

# função para converter as datas
def converter_data(data_str):
    try:
        return pd.to_datetime(data_str, format="%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return pd.to_datetime(data_str, format="%d/%m/%Y")
        except ValueError:
            return pd.NaT
        
# função para converter as horas
def converter_hora(hora_str):
    try:
        return pd.to_datetime(hora_str, format="%H:%M:%S").strftime("%H:%M")
    except ValueError:
        try:
            return pd.to_datetime(hora_str, format="%H:%M").strftime("%H:%M")
        except ValueError:
            return pd.NaT

# aplicar as funções ao dataframe
df['data'] = df['data'].apply(converter_data)
df['hora'] = df['hora'].apply(converter_hora)

df = df.reset_index(drop = True)

# print(df)

# salvar a base
df.to_excel('assets/protetor_natura.xlsx', sheet_name = 'protetor_natura', index = False)
