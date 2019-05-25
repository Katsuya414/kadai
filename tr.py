import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("https://folio-sec.com/theme/virtual-reality")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table", {"class":"TextMainLink__textMainLink--38tbe Instruments__instrumentName--4jzC9 gtm-stock-detail"})[1]
rows = table.findAll("tr")

with open("ebooks2.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
