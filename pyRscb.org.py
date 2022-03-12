# scraping data from text file from https://www.rcsb.org/

import requests
from bs4 import BeautifulSoup

kody = ["2GB1", "2PCY"]
main_url = "https://files.rcsb.org/view/"

for c in kody:
    url = main_url + c + ".pdb"
    out = requests.get(url)
    plik = open(c, "w")

    print(out.text)

    plik.close()
