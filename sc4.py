import requests, bs4

x = raw_input("Please Enter theme: ")

brands = []
res = requests.get('https://folio-sec.com/theme/' + "%s" % x)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.find_all(class_="TextMainLink__textMainLink--38tbe Instruments__instrumentName--4jzC9 gtm-stock-detail")
for elem in elems:

  brands.append(elem.text)

for brand in sorted(set(brands), key=brands.index):
  print(brand)
