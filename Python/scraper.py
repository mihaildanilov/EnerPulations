import requests
from bs4 import BeautifulSoup
import json

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Failed to retrieve the page: {response.status_code}')
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    data = []
    for i, table in enumerate(tables):
        rows = table.find_all('tr')[1:]  # Skipping header
        day = soup.find_all('h4')[i].text.strip()  # Adjusted day fetching
        for row in rows:
            cols = row.find_all('td')
            hour = cols[1].text.strip()
            price = cols[0].text.strip()
            data.append({"hour": hour, "price": price, "day": day})
    return data

# URL of the page to be scraped
url = 'https://www.e-cena.lv/'

# Fetching data
data = fetch_data(url)

# Outputting data as JSON for inspection
print(json.dumps(data, indent=4))
