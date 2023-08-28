from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass


class ByndyusoftPage(BaseClass):

    # Locators
    BUTTON_PRESENT = "//span[@class='btn btn--lg btn--info js-popup-callback-show']"
    EMAIL_PARS = "//div[@class='popup-callback__footer']//a[@href='mailto:sales@byndyusoft.com']"
    BUTTON_CLOSE_POPUP = "//i[@class='popup-callback__button-close js-popup-callback-hide']"

    # Getters
    def get_button_present(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_PRESENT)))

    def get_email_pars(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.EMAIL_PARS))).text

    def get_button_close_popup(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_CLOSE_POPUP)))

    # Actions
    def click_button_present(self):
        self.get_button_present().click()
        print("Click button present")

    def click_button_close_popup(self):
        self.get_button_close_popup().click()
        print("Click button close popup")

    # Metods
    def parsing_contacts(self):
        """Parsing Byndyusoft contacts"""

        self.click_button_present()
        assert self.get_email_pars() == "sales@byndyusoft.com", f"Email {self.get_email_pars()} is not found"
        self.click_button_close_popup()
