import requests
from bs4 import BeautifulSoup

response = requests.get('https://folio-sec.com/theme/virtual-reality')
soup = BeautifulSoup(response.text,'lxml')
twitter = soup.find('a',class_='PcOnly__pcOnly--20-xr').get('class')

print(twitter)
