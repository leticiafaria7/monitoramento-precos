# automação airbnb

# bibliotecas
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# parte do selenium

options = Options()
options.add_argument('--headless') # faz toda a rotina, mas o navegador não abre
options.add_argument('window-size=400,800') # define o tamanho da tela

navegador = webdriver.Chrome(options = options)
navegador.get('https://www.airbnb.com.br/')

sleep(2)

# printar o código da página
# print(BeautifulSoup(navegador.page_source, 'html.parser').prettify())

# clicar no campo que tem que pesquisar
qualquer_lugar = navegador.find_element(By.CSS_SELECTOR, 'button')
qualquer_lugar.click()

sleep(1)

# encontrar o elemento de entrada dentro do formulário
form = navegador.find_element(By.TAG_NAME, 'form')

# colocar o input
input_place = form.find_element(By.TAG_NAME, 'input')
# input_place.clear()
# input_place.send_keys(Keys.ENTER)
form.submit()

sleep(0.5)

# # clicar no primeiro botão que tem uma imagem dentro
# button_stay = navegador.find_element(By.CSS_SELECTOR, 'button > img')
# button_stay.click()

# sleep(0.5)

# print(BeautifulSoup(navegador.page_source, 'html.parser').prettify())

# clicar no último botão da página (next button)
next_button = navegador.find_element(By.CSS_SELECTOR, 'button > div[data-testid="dates-footer-primary-btn"]')
next_button.click()

# # definir 2 adultos
adult_button = navegador.find_element(By.CSS_SELECTOR, 'button > span > svg > path[d="m6.75.75v4.5h4.5v1.5h-4.5v4.5h-1.5v-4.5h-4.5v-1.5h4.5v-4.5z"]')
adult_button.click()
sleep(1)
adult_button.click()
sleep(1)

# # clicar no último botão da página (search button)
search_button = navegador.find_element(By.CSS_SELECTOR, 'button > span[class="tb4j57x dir dir-ltr"]')
search_button.click()

sleep(4)

# converter em objeto beautifulsoap
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# criar uma lista vazia para colocar os dados printados depois
dados_hospedagens = []

# print(site.prettify())

# pegar os apartamentos
hospedagens = site.findAll('div', attrs = {'itemprop': 'itemListElement'})
# print(hospedagens.prettify())

for hospedagem in hospedagens:

    # pegar o nome e a URL do primeiro apartamento
    hospedagem_descricao = hospedagem.find('meta', attrs = {"itemprop": 'name'})
    hospedagem_url = hospedagem.find('meta', attrs = {"itemprop": 'url'})

    hospedagem_descricao = hospedagem_descricao['content']
    hospedagem_url = hospedagem_url['content']

    print('Descrição: ', hospedagem_descricao) # printar só o nome do primeiro apartamento
    print('URL: ', hospedagem_url)
    print()

    # pegar os detalhes
    # hospedagem_detalhes = hospedagem.find('div', attrs = {'style': 'margin-bottom: 2px;'}).findAll('li')

    # 1. de forma manual
    # hospedagem_detalhes = hospedagem_detalhes[0].text + hospedagem_detalhes[1].text

    # # 2. com loop - compressão de listas
    # hospedagem_detalhes = ''.join([detalhe.text for detalhe in hospedagem_detalhes])
    # print('Detalhes da hospedagem: ', hospedagem_detalhes)

    # # pegar a info de preço
    # preco = hospedagem.findAll('span')[-1].text
    # print('Preço da hospedagem: ', preco)

    # print()

    dados_hospedagens.append([hospedagem_descricao, hospedagem_url])

# colocar em um dataframe
df = pd.DataFrame(dados_hospedagens, columns = ['Descricao', 'URL'])

# salvar como csv
df.to_csv('hospedagens.csv', index = False)





