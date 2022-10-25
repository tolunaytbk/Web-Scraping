import requests
from bs4 import BeautifulSoup
import pandas as pd

Url = "https://www.fishbase.org.au/country/CountryChecklist.php?showAll=yes&c_code=792&vhabitat=saltwater"
R = requests.get(Url)
Soup = BeautifulSoup(R.text, "html5lib")

url_head = "https://www.fishbase.org.au/country/"
Species = []
Urls = []
for a in Soup.find("table", {"class": "commonTable"}).find_all("a", href=True):
    species = a.text
    Species.append(species)
    url = url_head + a['href']
    Urls.append(url)

df1 = pd.DataFrame(Species, columns=['Species'])
df2 = pd.DataFrame(Urls, columns=['Urls'])

df = pd.concat([df1, df2], axis=1)

df.to_excel('urls.xlsx')
