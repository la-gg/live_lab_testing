# Look at this list of best-selling artists, particularly the table
# for those with more than 250m records sold:
# https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

# 1. Are we allowed to scrape the data from this page with a program?
#   What two things should we check?
# robots.txt
# Terms of use: check and check

# 2. Once verifying that we're allowed to, collect the 250m+ table
#   into a csv document.

import requests
import os
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path_folder = (r"/Users/alicelele/Desktop/UChicago/Masters/Spring '23 Classes"
               r"/Data and Programming for Public Policy I/Github"
               r"/live_lab_testing")

path = os.path.join(path_folder, 'wiki_table.csv')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

'Beatles' in soup.text

tables = soup.find_all('table')

print(len(tables))

table = tables[0]


rows = table.find_all('tr')

print(len(rows))

# Focusing in on just the Beatles
th_tags = rows[1].find_all('th')
td_tags = rows[1].find_all('td')
# or
tags = rows[1].find_all(['th', 'td'])

tags_clean = [val.text for val in tags]
tags_cleaner = [val.text.strip().replace('\n', ' ') for val in tags]
tags_cleanest = [val.text.strip().replace('\n', ' ').replace(',', '')
                 for val in tags]

for row in rows ...
