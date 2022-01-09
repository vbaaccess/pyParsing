from typing import Set
import requests
from bs4 import BeautifulSoup
import re

def get_recepie_links(keyword: str) -> Set[str]:
    """
    Extracting links from search engine with recipes.
    """
    recepie_links = set()
    url ='https://www.kwestiasmaku.com'
    adres = url +'/szukaj?search_api_views_fulltext={}'.format(keyword)
    response = requests.get(adres)
    soup = BeautifulSoup(response.content, 'html.parser')

    div = soup.select('div[class*="view-wyniki-wyszukiwania"]')

    divs = div[0].find_all('div', class_="field field-name-title field-type-ds field-label-hidden")
    for div in divs:
        result = re.search('"/(.*)">', str(div))
        recepie_links.add(url + '/' + result.group(1))

    return recepie_links
