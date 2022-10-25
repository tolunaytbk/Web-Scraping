import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

tic = time.process_time()

data = pd.read_excel("urls.xlsx")

Species = data['Species']
Urls = data['Urls']

n = 0
IUCN_status = []
ThreatForHumans = []
HumanUses = []
WL_urls = []
for url in Urls:
    R = requests.get(url)
    Soup = BeautifulSoup(R.text, "html5lib")
    status = Soup.find("div", {"class": "sleft sonehalf"}).find("div", {"class": "smallSpace"}).find("a").text
    print(n+1)
    print(status)
    IUCN_status.append(status)
    threat = Soup.find("div", {"class": "rlalign sonehalf"}).find("div", {"class": "smallSpace"}).text
    print(threat)
    ThreatForHumans.append(threat)
    uses = Soup.find("div", {"class": "rlalign sonehalf"}).find("div").find_next("h1", {"class": "slabel bottomBorder"})
    uses = uses.find_next("div").text
    print(uses)
    HumanUses.append(uses)
    str = f"Length-weight for {Species[n]}"
    n = n + 1
    url_head = "https://www.fishbase.org.au"
    a = Soup.find("div", {"id": "ss-moreinfo-container"}).find("a", {"alt": str}, href=True)
    if a is None:
        coef_url = "None"
    else:
        coef_url = url_head + a['href']
    print(coef_url)
    WL_urls.append(coef_url)

data['IUCN_status'] = IUCN_status
data['ThreatForHumans'] = ThreatForHumans
data['HumanUses'] = HumanUses
data['WL_urls'] = WL_urls

data.to_excel('features_tr_Marine.xlsx')

toc = time.process_time()
print(toc-tic)



