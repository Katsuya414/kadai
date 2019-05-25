import requests, bs4

x = raw_input("Please Enter theme: ")
res = requests.get('https://folio-sec.com/theme/' + "%s" % x)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.find_all(class_="SpOnly__spOnly--16kJq")
for elem in elems:
    print(elem.text)
