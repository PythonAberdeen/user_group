import requests
from bs4 import BeautifulSoup


def main():
    city_list = ["Perth,_Scotland", "Edinburgh", "Glasgow", "Aberdeen", "Stirling", "Inverness", "Dundee"]

    city_ids = {}
    city_pops = {}

    for city in city_list:
        city_ids[city] = get_id(city)

    for key, val in city_ids.items():
        city_pops[key] = scrape_data(val)

    print(city_pops)


def get_id(city):   # Scrape main Wikipedia page for WikiData id
    url = f"https://en.wikipedia.org/wiki/{city}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    raw_link = soup.find("li", {"id": "t-wikibase"})
    clean_url = raw_link.findChild("a")['href']
    data_id = clean_url.split("Q")
    full_id = "Q" + data_id[1]

    return full_id


def scrape_data(city_id):   # Scrape WikiData page for population figure.
    url = f"https://www.wikidata.org/wiki/{city_id}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    raw_div = soup.find("div", {"id": "P1082"})
    pop_val = raw_div.find("div",
                           {"class": "wikibase-snakview-value wikibase-snakview-variation-valuesnak"}).text.strip()

    return pop_val


if __name__ == '__main__':
    main()
