import time

from selenium import webdriver
from unittest import TestCase
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''Verificam ca mesajele de completare campuri obligatorii sunt afisate'''


class DisplayedMessages(TestCase):
    MAIN_URL = 'https://optoutccpa-devenv.bigdbm.com/'
    SUBMIT_BUTTON_SELECTOR = (By.CLASS_NAME, "btn-primary")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.MAIN_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(8)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_submit(self):
        submit_button = self.browser.find_element(by=By.CLASS_NAME, value="btn-primary")
        self.browser.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        submit_button.click()

    def test_msg_accept_terms(self):
        msg_accept_terms_found = False
        try:
            self.browser.find_element(By.ID, "validationForTerms")
            msg_accept_terms_found = True
        except NoSuchElementException:
            self.assertTrue(msg_accept_terms_found, "Accept terms message is not displayed.")

    def test_msg_select_option(self):
        try:
            self.browser.find_element(By.ID, "optOutTypeSelectedValidation")
        except NoSuchElementException:
            self.assertTrue(False, "Select option message is not displayed.")

    def test_msg_mandatory_fields(self):
        try:
            self.browser.find_element(By.ID, "validationForSubmit")
        except NoSuchElementException:
            self.assertTrue(False, "Mandatory fields message not displayed.")
