
def walker(soup):
    elements = soup.select("div.acalog-core")
    results = []

    for el in elements:
        heading = (el.select_one("h2, h3, h4")).get_text(strip=True)
        courses = []

        for course in el.select("li.acalog-course"):
            courses.append(course.get_text(strip=True))

        section = {"heading": heading, "courses": courses}

        results.append(section)

    return results
