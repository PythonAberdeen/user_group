import requests
from bs4 import BeautifulSoup


def main():
    # full_city_list = ["Perth,_Scotland", "Edinburgh", "Glasgow", "Aberdeen", "Stirling", "Inverness", "Dundee"]
    city_list1 = ["Perth,_Scotland", "Stirling", "Inverness"]

    for city in city_list1:
        get_pop_dat(city)


def get_pop_dat(city):
    url = f"https://en.wikipedia.org/wiki/{city}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    raw_table = soup.findAll("table", {"class": "infobox geography vcard"})

    cell = ""

    for h in raw_table[0].find_all("th"):
        if h.text.strip() == "Population":
            cell = h.parent.find_all("td")[0].text.strip()

    pop_dat = cell.split()[0]

    out_str = f"{city}: {pop_dat}"

    print(out_str)


if __name__ == '__main__':
    main()

