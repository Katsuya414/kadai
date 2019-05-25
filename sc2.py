import requests, bs4
n = 128
m = 140
res = requests.get('https://folio-sec.com/theme/virtual-reality')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.find_all(class_="TextMainLink__textMainLink--38tbe Instruments__instrumentName--4jzC9 gtm-stock-detail", role="link", type="button")
for elem in elems:
    print(elem)
