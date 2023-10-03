
##################################################################################################################################################################
# bibliotecas
##################################################################################################################################################################

import pandas as pd
import datetime

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

options = Options()
options.add_argument('--headless') # faz toda a rotina, mas o navegador não abre
options.add_argument('window-size=1500,800') # define o tamanho da tela

navegador = webdriver.Chrome(options = options)
navegador.get('https://www.amazon.com.br/Garmin-Forerunner%C2%AE-Music-smartwatch-corrida/dp/B09WTJ48NB')

sleep(2)

# converter em objeto beautifulsoap
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# criar uma lista vazia para colocar os dados printados depois
monitoramento_preco = []

# pegar o preço no site
reais = site.find('span', attrs = {'class': 'a-price-whole'})
centavos = site.find('span', attrs = {'class': 'a-price-fraction'})

# arrumar o preco
preco = reais.text + centavos.text
preco = preco.replace(".", "")
preco = preco.replace(",", ".")

# salvar a data e a hora atual em variáveis
data = datetime.date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().time().strftime("%H:%M")

# fazer o append na lista
monitoramento_preco.append([data,
                            hora,
                            preco,
                            'amazon',
                            'preto'])

# colocar em um dataframe
df = pd.DataFrame(monitoramento_preco, columns = ['data', 'hora', 'preco', 'site', 'cor'])
df['preco'] = df['preco'].astype('float')

# chamar a base já existente e concatenar o novo preço
base = pd.read_excel('assets/forerunner_255s.xlsx', 'forerunner_255s', engine = 'openpyxl')
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

# salvar a base
df.to_excel('assets/forerunner_255s.xlsx', sheet_name = 'forerunner_255s', index = False)
