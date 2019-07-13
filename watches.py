import re
import requests
from bs4 import BeautifulSoup
from math import ceil

USERNAME = ""
# Enter your Username here

ALL_WATCHES = []

# Constants
profile = "https://furaffinity.net/user/"
watchlist = "https://furaffinity.net/watchlist/by/{}/{}"

page = requests.get(profile + USERNAME)
soup = BeautifulSoup(page.content, 'html.parser')

amount = soup.find(
    'a',
    href=re.compile("^/watchlist/by/")
).get_text()

watches = int(''.join([i for i in amount if i.isdigit()]))
pages = ceil(watches/200)

for page in range(pages):
    print("Getting Page", page+1)
    watch = requests.get(watchlist.format(USERNAME, page+1))
    soup = BeautifulSoup(watch.content, 'html.parser')
    for x in soup.find_all('span', {'class': 'artist_name'}):
        ALL_WATCHES.append(x.get_text().strip('_'))

with open(USERNAME+'.txt', 'w') as f:
    for x in ALL_WATCHES:
        f.write(x)
