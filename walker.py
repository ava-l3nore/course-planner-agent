
def walker(soup):
    elements = soup.select("h2, h3, h4, li.acalog-course, li.acalog-adhoc")
    result = []

    # get information from soup-- grouped by section
    #for el in elements:

    print(elements)

    #return result
