import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

tic = time.process_time()

data = pd.read_excel('features_tr_Marine.xlsx')
print(data.columns)

Urls = data['WL_urls']
missing_url = "None"

n = 0
geometric_mean_a = []
mean_b = []
SD_log_w = []
SD_log_a = []
SD_b = []
for url in Urls:
    print(n + 1)
    if url == missing_url:
        print("No URL")
        geometric_mean_a.append(None)
        mean_b.append(None)
        SD_log_w.append(None)
        SD_log_a.append(None)
        SD_b.append(None)
        n = n + 1
    else:
        R = requests.get(url)
        Soup = BeautifulSoup(R.text, 'html5lib')

        # Geometric Mean a
        mean_a = Soup.find("input", {"id": "geomMeanA"}, value=True)
        print(f"geomMeanA: {mean_a['value']}")
        if mean_a['value'] is None:
            geometric_mean_a.append("No_data")
        else:
            geometric_mean_a.append(mean_a['value'])
        # Mean b
        mean_b1 = Soup.find("input", {"id": "mean_b"}, value=True)
        print(f"mean_b: {mean_b1['value']}")
        if mean_b1['value'] is None:
            mean_b.append("No_data")
        else:
            mean_b.append(mean_b1['value'])
        # SD log10(W)
        sdLogW = Soup.find("input", {"id": "sdLogW"}, value=True)
        print(f"SD log10(W): {sdLogW['value']}")
        if sdLogW['value'] is None:
            SD_log_w.append("No_data")
        else:
            SD_log_w.append(sdLogW['value'])
        # SD log10(a)
        sdLogA = Soup.find("input", {"id": "sdLogA"}, value=True)
        print(f"SD log10(a): {sdLogA['value']}")
        if sdLogA['value'] is None:
            SD_log_a.append("No_data")
        else:
            SD_log_a.append(sdLogA['value'])
        # SD b
        sd_b = Soup.find("input", {"id": "sd_b"}, value=True)
        print(f"SD b: {sd_b['value']}")
        if sd_b['value'] is None:
            SD_b.append("No_data")
        else:
            SD_b.append(sd_b['value'])
        n = n+1

data['geometric_mean_a'] = geometric_mean_a
data['mean_b'] = mean_b
data['SD_log_w'] = SD_log_w
data['SD_log_a'] = SD_log_a
data['SD_b'] = SD_b

data.to_excel('Tr_Marine_Species_ALL.xlsx')

toc = time.process_time()
print(toc-tic)
