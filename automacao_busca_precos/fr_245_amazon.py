
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
from formatacao_data_hora import converter_data, converter_hora

##################################################################################################################################################################
# parte do selenium
##################################################################################################################################################################

options = Options()
options.add_argument('--headless') # faz toda a rotina, mas o navegador não abre
options.add_argument('window-size=1500,800') # define o tamanho da tela

navegador = webdriver.Chrome(options = options)
navegador.get('https://www.amazon.com.br/Esportivo-Garmin-Forerunner-Vermelho-Card%C3%ADaco/dp/B07RG5VCFT/ref=d_pd_vtp_sccl_2_3/133-9424469-2772417?pd_rd_w=NFm5C&content-id=amzn1.sym.38f285bf-51cf-4756-b852-81b03b491f92&pf_rd_p=38f285bf-51cf-4756-b852-81b03b491f92&pf_rd_r=Z1M3R65AM1N4RC825E3M&pd_rd_wg=SJiM7&pd_rd_r=956eaa46-c16e-4301-9074-bafe2aa70cc1&pd_rd_i=B07RG5VCFT&th=1')

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

# print(preco)

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
base = pd.read_excel('../assets/forerunner_245.xlsx', 'forerunner_245', engine = 'openpyxl')
df = pd.concat([base, df])

# aplicar as funções ao dataframe
df['data'] = df['data'].apply(converter_data)
df['hora'] = df['hora'].apply(converter_hora)

df = df.reset_index(drop = True)

# print(df)

# salvar a base
df.to_excel('../assets/forerunner_245.xlsx', sheet_name = 'forerunner_245', index = False)
