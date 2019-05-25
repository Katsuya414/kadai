import requests
from bs4 import BeautifulSoup

response = requests.get('https://folio-sec.com/theme/virtual-reality')
soup = BeautifulSoup(response.text,'lxml')
title = soup.title.string
print(title)
