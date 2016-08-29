from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SearchClasses import GalleryList


#SEARCH_PHRASE = "Cal Ripken 1982 Fleer PSA 10 card #176"
SEARCH_PHRASE = "baseball"
sites = []
sites.append({
    "name": "Albersheims",
    "url": "http://albersheims.com/",
    "element": "id",
    "searchbox": "query",
    "results_container": "galleryList",
    "resultsTagName": "li",
    "class": "GalleryList",
    "submit": "SearchBtn",
})


def main():
    browser = webdriver.Firefox()
    for site in sites:
        search_for_card(site, browser)

def search_for_card(website, browser):
    browser.get(website['url'])
    search_box = browser.find_element_by_id(website['searchbox'])
    search_box.send_keys(SEARCH_PHRASE)
    browser.find_element_by_id(website['submit']).click()
    classname = website['class']
    searchClass = globals()[classname](website, browser)
    if searchClass.search_website():
        print "Possible match found at: {}".format(website['name'])
    else:
        print "No matches found"

if __name__ == "__main__":
    main()
