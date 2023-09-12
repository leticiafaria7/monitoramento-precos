# Busca automatizada por produtos - Mercado Livre

# bibliotecas
import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('Qual produto você deseja? ')
response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

# pegar todos os produtos
produtos = site.findAll('div', attrs = {'class': 'andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16'})

# loop para pegar as informações dos produtos
for produto in produtos:

    titulo = produto.find('h2', attrs = {'class': 'ui-search-item__title shops__item-title'})
    link = produto.find('a', attrs = {'class': 'ui-search-link'})
    real = produto.find('span', attrs = {'class': 'andes-money-amount__fraction'})

    # print(produto.prettify())
    print(titulo.text)
    print(link['href'])
    print(real.text)
    print('\n\n')


