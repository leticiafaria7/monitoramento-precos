# automação airbnb

# bibliotecas
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

# parte do selenium

options = Options()
# options.add_argument('--headless') # faz toda a rotina, mas o navegador não abre
options.add_argument('window-size=400,800') # define o tamanho da tela

navegador = webdriver.Chrome(options = options)
navegador.get('https://www.airbnb.com.br/?_set_bev_on_new_domain=1695251287_MjE0NTkzMWIyMTdm')

sleep(2)

input_place = navegador.find_element(By.TAG_NAME, 'input')
input_place.send_keys('São Paulo')
input_place.submit() # enter

sleep(0.5)

# clicar no primeiro botão que tem uma imagem dentro
button_stay = navegador.find_element(By.CSS_SELECTOR, 'button > img')
button_stay.click()

sleep(0.5)

# clicar no último botão da página (next button)
next_button = navegador.find_element(By.TAG_NAME, 'button')[-1]
next_button.click()

# definir 2 adultos
adult_button = navegador.find_element(By.CSS_SELECTOR, 'button > span > svg > path[d="m2 16h28m-14-14v28"]')[0]
adult_button.click()
sleep(1)
adult_button.click()
sleep(1)

# clicar no último botão da página (search button)
search_button = navegador.find_element(By.TAG_NAME, 'button')[-1]
search_button.click()

sleep(4)

# converter em objeto beautifulsoap
page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# pegar os apartamentos
hospedagem = site.find('div', attrs = {'itemprop': 'itemListElement'})
# print(hospedagem.prettify())

# pegar o nome do primeiro apartamento
hospedagem_descricao = hospedagem.find('meta', attrs = {"itemprop": 'name'})
hospedagem_url = hospedagem.find('meta', attrs = {"itemprop": 'url'})
print('Descrição: ', hospedagem_descricao['content']) # printar só o nome do primeiro apartamento
print('URL: ', hospedagem_url['content'])

hospedagem_detalhes = hospedagem.find('div', attrs = {'style': 'margin-bottom: 2px;'}).findAll('li')

# print(input_place)
# print(navegador.page_source) # ver o código da página
# parte do beautifulsoap

# site = BeautifulSoup(navegador.page_source, 'html.parser')
# print(site.prettify())





