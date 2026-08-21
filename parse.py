from bs4 import BeautifulSoup
import fetch

def parse(major, URL):
    soup = BeautifulSoup(fetch.fetch(major, URL), "html.parser")
    print("courses found:", len(soup.select("li.acalog-course")))


    print("courses: ")
    print("-------------------------")
    for i, course in enumerate(soup.select("li.acalog-course")):
        print(f"{i}) {course.get_text(strip=True)}")
        

    return soup