import os
import ntpath
import urllib3
import shutil

url_target = "https://nofluffjobs.com/pl/praca-it/python"
fileName = ntpath.basename(url_target) + "_20220312.txt"
path = os.getcwd() + os.path.sep + fileName


print("path:", path)

print(20*"-", "Analiza pliku", 20*"-")
print("      url:", url_target)
print("file name:", fileName)
print(60*"-")

if not os.path.isfile(path):
    print("... brak pliku lokalnego, pobieram plik...")
    # STEP 1
    http = urllib3.PoolManager()
    with http.request('GET', url_target, preload_content=False) as r, open(path, 'wb') as out_file:
        shutil.copyfileobj(r, out_file)
else:
    print("Odnaleziono zapisany plik lokalny:")
    print(path)

# przetwarzanie pliku
from bs4 import BeautifulSoup

print("Pobranie danych z plik do dalszej analizy (for BeautifulSoup ):")
print(60*"-")
with open(path, 'r') as objFile:
    out = objFile.read()
    soup = BeautifulSoup(out, 'html.parser')

print("Przetwarzanie plik lokalny:")
div = soup.select('div[class*="text-center mt-5 ng-star-inserted"]')
print(div[0].find_all("a"))

tag_list = list(div[0].find_all("a"))
# href_list = soup.select('div[class*="page-link"]') # tagi z hrrr, tylko wg konkretnie nazwanej klasy

for tag in tag_list:
    print(tag.string, type(tag.string))

print(len(tag_list))
url_count = int(tag_list[-2].string)


for urlLp in range(1,url_count+1):
    url = url_target + "?page=" + str(urlLp)
    print(urlLp, ")", url)
