import time

from pages.byndyusoft_page import ByndyusoftPage
from pages.google_page import GooglePage


def test_byndyusoft(browser):
    link = "https://google.com"
    print("\nStart test parsing contacts")
    browser.maximize_window()
    gp = GooglePage(browser, link)
    gp.open()
    gp.search_byndyusoft_by_google()

    bp = ByndyusoftPage(browser, link)
    bp.parsing_contacts()

    print("\nEnd test parsing contacts")
    time.sleep(1)
