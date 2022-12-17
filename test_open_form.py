from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

''' Verificam ca se deschide pagina web/ formularul corect'''


class OpenPage(TestCase):
    MAIN_URL = 'https://optoutccpa-devenv.bigdbm.com/'

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.MAIN_URL)
        self.browser.maximize_window()
        self.browser.implicitly_wait(8)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_correct_page_name(self) -> None:
        self.assertEqual(self.browser.title, "Home Page - Consumer Rights Requests", "Incorrect page title")
        print(self.browser.current_url)

