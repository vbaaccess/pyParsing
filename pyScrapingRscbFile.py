import requests

kody = ["2GB1", "2PCY"]
main_url = "https://files.rcsb.org/view/"

for c in kody:
    # url = "https://files.rcsb.org/view/2GB1.pdb"
    url = main_url + c + ".pdb"
    out = requests.get(url)
    plik = open(c, "w")
    # print(out.text, file=plik)
    print(out.text)

    plik.close()
    
