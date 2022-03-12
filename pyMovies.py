import requests
from bs4 import BeautifulSoup

main_url = "https://www.imdb.com/chart/top/"

for c in kody:
  url = main_url + c + ".pdb"
  out = requests.get(url)
  plik = open(c,"w")
  print(out.text)

  plik.close()
