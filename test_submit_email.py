import time

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


'''Verificam ca putem trimite formularul doar cu "2 First Name, Last Name, and the Email."
    asa cum este mentionat in mesaj'''


class SubmitFormEmail(TestCase):
    MAIN_URL = 'https://optoutccpa-devenv.bigdbm.com/'
    AGREEMENT_BOX_SELECTOR = (By.ID, "inlineFormCheck")
    SUBMIT_BUTTON_SELECTOR = (By.CLASS_NAME, "btn-primary")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.MAIN_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_submit_email(self):
        specific_box = self.browser.find_element(by=By.ID, value="formCheckSpecial")
        first_name = self.browser.find_element(value="horizontal-firstname-input")
        last_name = self.browser.find_element(value="horizontal-lastname-input")
        email = self.browser.find_element(value="horizontal-email-input")
        agreement = self.browser.find_element(*self.AGREEMENT_BOX_SELECTOR)
        submit_button = self.browser.find_element(*self.SUBMIT_BUTTON_SELECTOR)

        specific_box.click()
        first_name.send_keys("LIDIA")
        last_name.send_keys("TEST - EMAIL")
        email.send_keys("lidia@bigdbm.com")
        self.browser.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        agreement.click()
        submit_button.click()
        time.sleep(4)
        self.assertEqual(self.browser.current_url, f"{self.MAIN_URL}Home/SaveConsumer",
                         'Formularul nu a fost trimis')
