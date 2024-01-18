import requests
from bs4 import BeautifulSoup

#129.79 | 132.55 | 131.47 | 128.13 | 128.4 | 125.17

#scraper
def scraper():
    page = requests.get("https://finance.yahoo.com/quote/AMZN?p=AMZN")
    soup = BeautifulSoup(page.content, 'html.parser')

    global item
    item = soup.find("td", {"class": "Ta(end) Fw(600) Lh(14px)"})

#end of game
def end(money, userStock):
    print("You ended the game here are your stats:")
    print(money)
    print(userStock)

    if money <= 400 or userStocks <= 2:
        print("DO BETTER")
    else:
        print("Well done")


stop = False


while(stop == False):
    scraper()
    invalid = False

    #to get the thing from the long thing
    thing = str(item)
    list = thing.split("<")
    list = str(list)
    list = list.split(">")
    ye = list[1]
    yeList = ye.split("'")

    stockVal = yeList[0]

    #the acctual game
    stockVal = float(stockVal)

    money = float(500)
    userStocks = 0

    print("")
    print("You have £", money, sep="")
    print("You have", userStocks, "stocks")
    print("")
    print("Todays stock price is £", stockVal, sep="")

    try:
        choice = int(input("Do you want to: Buy(1) Sell(2) Skip(0): "))
    except:
        invalid = True
        print("Invalid input")


    if invalid == False and choice <= 3 or choice >= 0:
        #buying
        if choice == 1 and money >= stockVal:
            amount = int(input("how many stocks do you want to buy(1-3): "))

            if amount >= 1 or amount <= 3:
                while(stockVal * amount > money):
                    print("You cannot afford", amount, "stocks")
                    amount = int(input("how many stocks do you want to buy(1-3): "))
                else:
                    userStocks += amount
                    money -= stockVal
            else:
                print("Invalid Input")

        #sell
        elif choice == 2:
            sellAmount = input("How many do you want to sell(1-3):")
            while sellAmount < userStocks:
                print("You do not have enough")
            else:
                userStocks -= sellAmount
                money += sellAmount * stockVal
        else:
            print("You have skipped today")
        input("")
    
    else:
        input("")

else:
    print("You have £", money, sep="")
    print("You have", userStocks, "stocks")

