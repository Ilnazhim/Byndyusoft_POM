from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.data import DataPage
from base.base_class import BaseClass


class GooglePage(BaseClass):

    # Locators
    GOOGLE_SEARCH_FIELD = "//textarea[@id='APjFqb']"
    BYNDYUSOFT_SITE = "//h3[normalize-space()='Byndyusoft']"

    # Getters
    def get_google_search_field(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.GOOGLE_SEARCH_FIELD)))

    def get_byndyusoft_site(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.BYNDYUSOFT_SITE)))

    # Actions
    def input_byndyusoft(self):
        self.get_google_search_field().send_keys(*DataPage.request)
        print("Input Byndyusoft for search")

    def click_byndyusoft_site(self):
        self.get_byndyusoft_site().click()
        print("Click Byndyusoft site")

    # Metods
    def search_byndyusoft_by_google(self):
        """Search Byndyusoft"""
        self.input_byndyusoft()
        self.click_byndyusoft_site()
        print("Open Byndyusoft site")
