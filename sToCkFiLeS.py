import requests
from bs4 import BeautifulSoup
import time
import csv

no = True
while(no):
    page = requests.get("https://finance.yahoo.com/quote/AMZN?p=AMZN")
    soup = BeautifulSoup(page.content, 'html.parser')
    item = soup.find("td", {"class": "Ta(end) Fw(600) Lh(14px)"})

    thing = str(item)
    list = thing.split("<")
    list = str(list)
    list = list.split(">")
    ye = list[1]
    yeList = ye.split("'")
    stockVal = yeList[0]
    stockVal = float(stockVal)

    stockList = [129.79, 132.55, 131.47, 128.13, 128.4, 125.17]

    stockList.append(stockVal)
    time.sleep(720)
    print(stockList)
    
    with open('ahh.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(stockList)
    

