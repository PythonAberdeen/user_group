import requests     # Get URLS
from bs4 import BeautifulSoup       # Web scrap


def find_super_bowl_champs():
    url = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', class_='wikitable sortable')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    rows.pop(0)
    rows.pop()

    winners = []

    for row in rows:
        data = row.find_all('td')[2].find("a").get_text()
        winners.append(data)

    print(winners)


def find_indian_capitals():
    url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', class_='wikitable sortable plainrowheaders')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    rows.pop(0)

    administrative = []
    legislative = []
    judicial = []

    for row in rows:
        administrative.append(row.find_all('td')[1].find("a").get_text())
        legislative.append(row.find_all('td')[2].get_text()[:-1])       #Non-Links aren't in <a> tags
        judicial.append(row.find_all('td')[3].get_text()[:-1])       #Non-Links aren't in <a> tags

    print(administrative)
    print(legislative)
    print(judicial)


find_super_bowl_champs()
find_indian_capitals()
