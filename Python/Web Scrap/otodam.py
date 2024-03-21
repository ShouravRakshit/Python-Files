import requests
from bs4 import BeautifulSoup

URL = "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?ownerTypeSingleSelect=ALL&distanceRadius=0&viewType=listing"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# You would then locate the elements you want to extract. For example:
items = soup.find_all('div', class_='item')  # This is just a placeholder, you'll need to inspect the page's source code to get the correct tag and class.

for item in items:
    # Extract and print the desired data from each item
    print(item.text)

