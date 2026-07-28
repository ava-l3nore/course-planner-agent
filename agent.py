import requests
from bs4 import BeautifulSoup

html = requests.get('https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6311').text
soup = BeautifulSoup(html, "html.parser")

for item in soup.select("li.acalog-course"):
    print(item.get_text(strip=True))