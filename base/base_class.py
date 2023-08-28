

class BaseClass:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    """Metod open browser"""
    def open(self):
        self.browser.get(self.url)
