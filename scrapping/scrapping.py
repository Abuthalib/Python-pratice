import requests
from bs4 import BeautifulSoup

website_url = "https://infopark.in/companies/job"
res = requests.get(website_url)
soup = BeautifulSoup(res.text, 'lxml')
allumini = soup.find_all("div", {"class": "grid-item"})
print(allumini)
