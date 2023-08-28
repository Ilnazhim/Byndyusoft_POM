import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():

    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nquit browser..")
