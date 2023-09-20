# selenium - web driver (controla o navegador) - navegador automatizado (entra na página e solicita o conteúdo)
# o beautiful soap não consegue pegar informações de alguns sites
# single page application - desenvolvidas usando react por ex - o navegador deve fazer a requisição para que o html seja montado no momento que o usuário pede pela página

# passos:
# instalar selenium (pip install selenium)
# instalar driver (https://selenium-python.readthedocs.io/installation.html) - ferramenta que permite integrar o código python com o navegador
# olhar a versão do chrome -> ir no chrome -> ... -> ajuda -> sobre o google chrome -> olhar qual a versão -> instalar o driver compatível

# bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# método que retorna o próprio navegador
navegador = webdriver.Chrome()

# acessar uma página
navegador.get('https://www.walissonsilva.com/blog')

sleep(3)

# encontrar elemento por TAG_NAME
elemento = navegador.find_element(By.TAG_NAME, 'input')

# ver se deu bom
# print(elemento)

elemento.send_keys('data')


