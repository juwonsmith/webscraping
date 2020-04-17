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
                print(i.text).replace("\n", "")
            for i in corona_soup.findAll("div", {"style" : "color:#8ACA2B "}):
                print("recovered:")
                print(i.text) 

    conc = input("please enter the country name: ")
    print("please restart and enter a country")
    some_country = get_corona(conc)
except :
    print("there has been an error ")
