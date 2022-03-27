import os
import ntpath
import urllib3
import shutil

import datetime
import time
import random


def download_url(url_target: str, filename_prefix: str = ""):
    if len(filename_prefix) == 0:
        filename_prefix = f"{datetime.datetime.now():%Y%m%d_}"

    filename = ntpath.basename(url_target)
    filename = filename.replace("?", "_")
    filename = filename.replace("=", "_")
    filename = filename_prefix + filename + ".txt"

    full_path = os.getcwd() + os.path.sep + 'download' + os.path.sep

    print(20*"-", "Analiza pliku", 20*"-")
    print("     url:", url_target)
    print("    path:", full_path)
    print("filename:", filename)
    print(60*"-")

    if not os.path.isfile(full_path + filename):
        print("... brak pliku lokalnego, pobieram plik...")
        # STEP 1
        time.sleep(random.randint(5, 10))
        http = urllib3.PoolManager()
        with http.request('GET', url_target, preload_content=False) as r, open(full_path + filename, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
    else:
        print("Odnaleziono zapisany plik lokalny:")
        print(full_path + filename)

    return full_path + filename
