import requests
from bs4 import BeautifulSoup

response = requests.get('https://folio-sec.com/theme/virtual-reality')
soup = BeautifulSoup(response.text,'lxml')
links = soup.findAll('a')
for link in links:
   print(link.get('href'))
