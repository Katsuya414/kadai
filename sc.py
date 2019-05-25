import requests
from bs4 import BeautifulSoup

response = requests.get('http://test.neet-ai.com')
soup = BeautifulSoup(response.text,'lxml')
title = soup.title.string
print(title)
