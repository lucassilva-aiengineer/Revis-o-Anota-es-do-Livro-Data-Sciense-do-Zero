# Extaindo dados da internet 


# WEB SCRAPING 
from bs4 import BeautifulSoup 
import requests 
import sys 


def acessando_paginas_html():

    url = "https://www.bibliaon.com/"
    url_2 = "https://www.bible.com/pt"

    if requests.get(url_2).status_code != 200: 
        print("Requisão mal sucedida!")
        sys.exit(1)

    html = requests.get(url_2).text 
    soup = BeautifulSoup(html, 'html5lib')

    primeiro_paragrafo = soup.find('p')

    print(primeiro_paragrafo)

acessando_paginas_html()