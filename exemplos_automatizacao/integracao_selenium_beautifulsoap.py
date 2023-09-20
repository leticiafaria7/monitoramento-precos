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

# clicar no último botão da página (search button)
search_button = navegador.find_element(By.TAG_NAME, 'button')[-1]
search_button.click()

sleep(4)

# converter em objeto beautifulsoap
page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

# print(input_place)
# print(navegador.page_source) # ver o código da página
# parte do beautifulsoap

# site = BeautifulSoup(navegador.page_source, 'html.parser')
# print(site.prettify())





