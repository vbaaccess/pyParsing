import os
import ntpath
import urllib3
import shutil

import datetime
import time
import random


sData = f"{datetime.datetime.now():%Y%m%d_}"

def download_url(url_target):
    filename = ntpath.basename(url_target)
    filename = filename.replace("?", "_")
    filename = filename.replace("=", "_")
    filename = sData + filename + ".txt"

    path = os.getcwd() + os.path.sep

    print(20*"-", "Analiza pliku", 20*"-")
    print("     url:", url_target)
    print("    path:", path)
    print("filename:", filename)
    print(60*"-")

    if not os.path.isfile(path + filename):
        print("... brak pliku lokalnego, pobieram plik...")
        # STEP 1
        time.sleep(random.randint(1, 3))
        http = urllib3.PoolManager()
        with http.request('GET', url_target, preload_content=False) as r, open(path + filename, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
    else:
        print("Odnaleziono zapisany plik lokalny:")
        print(path + filename)

    return path + filename


url_target = "https://nofluffjobs.com/pl/praca-it/python"
# filename_target = ntpath.basename(url_target) + ".txt"
path = download_url(url_target)


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
# print("penultimate = >", url_count, type(url_count))

list_of_pages = []
for urlLp in range(1,url_count+1):
    url = url_target + "?page=" + str(urlLp)
    path = download_url(url)
    print(urlLp, ")", url, "=>" , path)
    list_of_pages.append(path)

for path in list_of_pages:
    print("path =>", path)
    # with open(path, 'r') as objFile:
    #     out = objFile.read()
    #     soup = BeautifulSoup(out, 'html.parser')
    #
    # print("Przetwarzanie podstrony zapisanej lokalnie:", path)
    # divs = soup.select('div[class*="list-container ng-star-inserted"]')
    # #print(divs)
    # for div in divs:
    #     print(div)

# test one page
with open(list_of_pages[0], 'r') as objFile:
    print("test", list_of_pages[0])
    out = objFile.read()
    soup = BeautifulSoup(out, 'html.parser')
    print(soup)
    div = soup.find('div[class*="posting"]')
    print(div)
