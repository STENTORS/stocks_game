import requests
from bs4 import BeautifulSoup
import time
import csv
#from datetime import date

#scraper
def scraper():
    page = requests.get("https://finance.yahoo.com/quote/AMZN?p=AMZN")
    soup = BeautifulSoup(page.content, 'html.parser')

    global item
    item = soup.find("td", {"class": "Ta(end) Fw(600) Lh(14px)"})

scraper()

thing = str(item)
list = thing.split("<")
list = str(list)
list = list.split(">")
ye = list[1]
yeList = ye.split("'")
stockVal = yeList[0]
stockVal = float(stockVal)

#today = date.today()

header = ["Stock"]
data = [stockVal]
filename = "!_!.csv"

with open('filename.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(stockVal)




