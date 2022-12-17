import requests
from bs4 import BeautifulSoup

menu=[]
price=[]

page=1
while page != 20:
      url = f"https://www.mcdelivery.eg/eg/browse/menu.html?daypartId=1&catId={page}"
      result = requests.get(url)
      src = result.content
      soup= BeautifulSoup(src, "lxml")
      page = page + 1
      menu = soup.find_all("h5", {"class": "product-title"})
      price = soup.find_all("span", {"class": "starting-price"})
      for i in range(len(menu)):
          menu.append(menu[i].text)
          print(menu[i].text)

          price.append(price[i].text)
          print(price[i].text)





