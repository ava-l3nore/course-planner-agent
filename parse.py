from bs4 import BeautifulSoup
import fetch

def parse(URL):
    soup = BeautifulSoup(fetch.fetch(URL), "html.parser")
    print("courses found:", len(soup.select("li.acalog-course")))