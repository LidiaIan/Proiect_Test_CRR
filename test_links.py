import time

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


'''Verificam ca putem accesa linkurile din pagina'''


class AccessLinks(TestCase):
    MAIN_URL = 'https://optoutccpa-devenv.bigdbm.com/'
    PRIVACY_POLICY_URL = 'https://bigdbm.com/privacy.html'
    OPT_OUT_URL = 'https://optout.bigdbm.com/'

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.MAIN_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_privacy_page(self):
        privacy_link = self.browser.find_element(by=By.LINK_TEXT, value='Privacy')
        time.sleep(4)
        privacy_link.click()
        time.sleep(3)
        self.assertEqual(self.browser.current_url, f"{self.PRIVACY_POLICY_URL}",
                         'Pagina de Privacy Policy nu poate fi accesata')
        print(self.browser.current_url)

    def test_opt_out_of_sale(self):
        opt_out_link = self.browser.find_element(by=By.LINK_TEXT, value='Opt Out of Sale')
        time.sleep(4)
        opt_out_link.click()
        time.sleep(3)
        self.assertEqual(self.browser.current_url, f"{self.OPT_OUT_URL}",
                         'Pagina de Opt Out of Sale nu poate fi accesata')
        print(self.browser.current_url)
