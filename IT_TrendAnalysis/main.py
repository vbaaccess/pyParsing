import configure
from helper import download_url
from dataclasses import dataclass


@dataclass
class BasicInformation:
    title: str
    description: str
    occupationalCategory: str
    datePosted: str


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
# print(40*"-")
# print("test", list_of_pages[0])
# pattern = "/pl/job/"
# patternLp = 0
# with open(list_of_pages[0], 'r', encoding="utf-8") as objFile:
#     out = objFile.read()
#     soup = BeautifulSoup(out, 'html.parser')
#
#     tags_a = soup.findAll("a", href=re.compile(pattern))
#     for tag_a in tags_a:
#         patternLp += 1
#         print(patternLp, ") href =>", tag_a["href"])

href_pattern = "/pl/job/"
hrefLp = 0
list_job = []
for pageLp, path_to_page in enumerate(list_of_pages):
    # print(pageLp, ") ", path_to_page)

    with open(path_to_page, 'r', encoding="utf-8") as objFile:
        out = objFile.read()
        soup = BeautifulSoup(out, 'html.parser')

        # tags_a = soup.findAll("a", href=re.compile(href_pattern))
        tags_a = soup.find_all("a", href=lambda href: href and href_pattern in href)
        for tag_a in tags_a:
            hrefLp += 1
            h = url_main + tag_a["href"]
            list_job.append(h)
            # print(hrefLp, ") href =>", h)

l = list_job
l = [j for j in l if "junior" in j]
l = [j for j in l if "python" in j]
l = [j for j in l if "remote" in j]

print("ilosc ofert", len(l))


