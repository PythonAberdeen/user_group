# import our libraries
import requests
from bs4 import BeautifulSoup

# WON'T WORK USING METHOD BELOW
#url = "https://en.wikipedia.org/wiki/Dundee"
#url = "https://en.wikipedia.org/wiki/Edinburgh"
#url = "https://en.wikipedia.org/wiki/Glasgow"
#url = "https://en.wikipedia.org/wiki/Aberdeen"

#WILL WORK USING METHOD BELOW
#url = "https://en.wikipedia.org/wiki/Perth,_Scotland"
#url = "https://en.wikipedia.org/wiki/Inverness"
url = "https://en.wikipedia.org/wiki/Stirling"


pop =int()
r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

rows = soup.find("table", {"class":"infobox geography vcard"}).find_all("tr")

for row in rows:
    cells = row.find_all("th")

    if cells and cells[0].get_text() == "Population":
        data_cells = row.find_all("td")
        pop = int(data_cells[0].get_text().split("(")[0].strip().replace(",",""))

print (pop)