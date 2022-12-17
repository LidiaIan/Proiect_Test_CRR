import time

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''Verificam ca putem trimite formularul doar cu "1 First Name, Last Name, Address1 and Zip Code"
        așa cum este mentionat in mesaj'''


class SubmitFormAddress(TestCase):
    MAIN_URL = 'https://optoutccpa-devenv.bigdbm.com/'
    AGREEMENT_BOX_SELECTOR = (By.ID, "inlineFormCheck")
    SUBMIT_BUTTON_SELECTOR = (By.CLASS_NAME, "btn-primary")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.MAIN_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(8)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_submit_address(self):
        specific_box = self.browser.find_element(by=By.ID, value="formCheckSpecial")
        first_name = self.browser.find_element(value="horizontal-firstname-input")
        last_name = self.browser.find_element(value="horizontal-lastname-input")
        address1 = self.browser.find_element(value="horizontal-address1-input")
        address2 = self.browser.find_element(value="horizontal-address2-input")
        city = self.browser.find_element(value="horizontal-city-input")
        zip_code = self.browser.find_element(value="horizontal-zip-input")
        agreement = self.browser.find_element(*self.AGREEMENT_BOX_SELECTOR)
        submit_button = self.browser.find_element(*self.SUBMIT_BUTTON_SELECTOR)

        specific_box.click()
        first_name.send_keys("LIDIA")
        last_name.send_keys("TEST - ADDRESS")
        address1.send_keys("Blv Eroilor, Nr 13")
        address2.send_keys("ap 68")
        city.send_keys("Cluj")
        zip_code.send_keys("12345")

        self.browser.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        agreement.click()
        submit_button.click()
        time.sleep(4)
        self.assertEqual(self.browser.current_url, f"{self.MAIN_URL}Home/SaveConsumer",
                         'Formularul nu a fost trimis')
