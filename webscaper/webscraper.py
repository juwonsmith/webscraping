import requests
from bs4 import BeautifulSoup
try:
    class get_corona:
            def __init__(self,country):
                self.country = country
                base_url = "https://www.worldometers.info/coronavirus/country/"
                loc = self.country+"/"
                url = base_url +  loc
                corona = requests.get(url)
                corona_soup= BeautifulSoup(corona.text, "html.parser")
                for i in corona_soup.findAll("div", {"style": "margin-top:15px"}):
                    print(i.text)
                for i in corona_soup.findAll("div", {"style" : "color:#8ACA2B "}):
                    print("recovered:")
                    print(i.text) 
    def call():
        print("this is a program to get the amount of people affected with coronavirus based on their country name")
        print()      
        conc = input("please enter the country name: ")
        if  conc == "" :
            x = input("you didnt input a country,do you want to restart the app,(yes/no): ")
            if x =="yes":
                call()
            else:
                print('thank you for your time')
        else:
            some_country = get_corona(conc)
    call()
except :
    print("there has been a connection error ")
