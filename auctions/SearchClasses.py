

class GalleryList:

    def __init__(self, siteDict, browser):
        self.siteDict = siteDict
        self.browser = browser

    def search_website(self):
        results = self.browser.find_element_by_id(self.siteDict['results_container'])
        results = results.find_elements_by_tag_name(self.siteDict['resultsTagName'])
        if len(results) > 0:
            return True
        else:
            return False

