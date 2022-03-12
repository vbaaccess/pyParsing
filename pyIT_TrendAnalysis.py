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

# podglad pliku
print("Podglad plik lokalny:")
print(60*"-")
with open(path, 'r') as objFile:
    print(objFile.readlines())
