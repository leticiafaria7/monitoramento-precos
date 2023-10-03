
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
navegador.get('https://www.mercadolivre.com.br/relogio-smartwatch-garmin-forerunner-255s-music-preto/p/MLB21406910?from=gshop&matt_tool=45720055&matt_word=&matt_source=google&matt_campaign_id=14303413811&matt_ad_group_id=134600901780&matt_match_type=&matt_network=g&matt_device=c&matt_creative=584295662843&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735128761&matt_product_id=MLB21406910-product&matt_product_partition_id=1800600541811&matt_target_id=pla-1800600541811&gclid=CjwKCAjwyNSoBhA9EiwA5aYlb7xSvk2dTaU9e79bWpdZVA8ItGdclDJDiRCMg0vWCzcJRvmS0iig7hoCXmAQAvD_BwE')

sleep(2)

# converter em objeto beautifulsoap
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# criar uma lista vazia para colocar os dados printados depois
monitoramento_preco = []

# pegar o preço no site
reais = site.find('span', attrs = {'class': 'andes-money-amount__fraction'})
# centavos = site.find('span', attrs = {'class': 'a-price-fraction'})
centavos = "00"

# arrumar o preco
preco = reais.text + "," + centavos
preco = preco.replace(".", "")
preco = preco.replace(",", ".")

# salvar a data e a hora atual em variáveis
data = datetime.date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().time().strftime("%H:%M")

# fazer o append na lista
monitoramento_preco.append([data,
                            hora,
                            preco,
                            'mercado livre',
                            'preto'])

# colocar em um dataframe
df = pd.DataFrame(monitoramento_preco, columns = ['data', 'hora', 'preco', 'site', 'cor'])
df['preco'] = df['preco'].astype('float')

# chamar a base já existente e concatenar o novo preço
base = pd.read_excel('../assets/forerunner_255s.xlsx', 'forerunner_255s', engine = 'openpyxl')
df = pd.concat([base, df])

# aplicar as funções ao dataframe
df['data'] = df['data'].apply(converter_data)
df['hora'] = df['hora'].apply(converter_hora)

df = df.reset_index(drop = True)

# salvar a base
df.to_excel('../assets/forerunner_255s.xlsx', sheet_name = 'forerunner_255s', index = False)
