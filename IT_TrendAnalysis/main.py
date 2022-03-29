from datetime import datetime

import configure
from helper import download_url
from dataclasses import dataclass


url_main = "https://nofluffjobs.com"
url_target = url_main + "/pl/praca-it/python"

path = download_url(url_target)

# przetwarzanie pliku
from bs4 import BeautifulSoup

print("Pobranie danych z plik do dalszej analizy (for BeautifulSoup ):")
print(60*"-")
with open(path, 'r', encoding="utf-8") as objFile:
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
for urlLp in range(1, url_count+1):
    url = url_target + "?page=" + str(urlLp)
    path = download_url(url)
    print(urlLp, ")", url, "=>", path)
    list_of_pages.append(path)

for path in list_of_pages:
    print("path =>", path)

href_pattern = "/pl/job/"
hrefLp = 0
list_job = []
for pageLp, path_to_page in enumerate(list_of_pages):

    with open(path_to_page, 'r', encoding="utf-8") as objFile:
        out = objFile.read()
        soup = BeautifulSoup(out, 'html.parser')

        # tags_a = soup.findAll("a", href=re.compile(href_pattern))
        tags_a = soup.find_all("a", href=lambda href: href and href_pattern in href)
        for tag_a in tags_a:
            hrefLp += 1
            h = url_main + tag_a["href"]
            list_job.append(h)

l = list_job
l = [j for j in l if "junior" in j]
l = [j for j in l if "python" in j]
l = [j for j in l if "remote" in j]

print("ilosc ofert", len(l))

list_of_jobs = []
#sDate = f"{datetime.datetime.now():%Y_}"
sDate = "2022_"
for jLp, url in enumerate(l):
    path = download_url(url, sDate)
    print(jLp+1, ")", url, "=>", path)
    list_of_jobs.append(path)

print("\nAnaliza ofert...")

import json

@dataclass
class BasicInformation:
    datePosted: datetime
    title: str
    description: str
    occupationalCategory: str
    datePosted: str

tag_start = '<script id="serverApp-state" type="application/json">'
tag_end = "</script>"

t = []
t.append(list_of_jobs[0])
for jLp, page in enumerate(t):
# for jLp, page in enumerate(list_of_jobs):
    print(jLp+1, ")", page)
    # print(jLp + 1, ")", page(re.compile("junior")))
    with open(page, 'r', encoding="utf-8") as objFile:
        out = objFile.read()
        soup = BeautifulSoup(out, 'html.parser')

    # JSON 1
    s = soup.find("script", type='application/ld+json')
    js = json.loads(s.string)
    # print(json.dumps(js, indent=10, sort_keys=True))
    print(json.dumps(js['@graph'][2], indent=10, sort_keys=True))

    # JSON 2
    s = str(soup.contents).split(tag_start)[1].split(tag_end)[0].replace("&q;", '"')
    js = json.loads(s)
    print(json.dumps(js['POSTING'], indent=10, sort_keys=True))

    # get data

    print("\nSzczegoly oferty:")
    print(json.dumps(js['POSTING']['details']['description'], indent=10, sort_keys=True))

    print("\nWymagania obowiazkowe:")
    print(json.dumps(js['POSTING']['requirements']['musts'], indent=10, sort_keys=True))

    print("\nMile widziane:")
    print(json.dumps(js['POSTING']['requirements']['nices'], indent=10, sort_keys=True))

    print("\nData Utworzenia:")
    print(json.dumps(js['POSTING']['details']['description'], indent=10, sort_keys=True))

    # JSON 1
    # JobPosting -> baseSalary -> value -> value
    # datePosted
    # description
    # jobLocation -> address -> addressLocality (remote)
    # search: python
    # search: Junior
    # search:  convertedSalary; range, currency

    # search: requirements -> muss...
    # search: nices -> muss...

    # JSON 2
