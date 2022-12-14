import time

from selenium import webdriver
from unittest import TestCase
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


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
        time.sleep(2)

    '''Verificam ca mesajele de completare campurii obligatorii sunt afisate'''


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
        # state = self.browser..find_element(value="")
        # state.send_keys("abfgfg")

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

    '''Verificam ca putem trimite formularul doar cu "3 First Name, Last Name, and Phone Number."
        asa cum este mentionat in mesaj'''


class SubmitFormPhone(TestCase):
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

    def test_submit_phone(self):
        specific_box = self.browser.find_element(by=By.ID, value="formCheckSpecial")
        first_name = self.browser.find_element(value="horizontal-firstname-input")
        last_name = self.browser.find_element(value="horizontal-lastname-input")
        phone = self.browser.find_element(value="horizontal-phone-input")
        agreement = self.browser.find_element(*self.AGREEMENT_BOX_SELECTOR)
        submit_button = self.browser.find_element(*self.SUBMIT_BUTTON_SELECTOR)

        specific_box.click()
        first_name.send_keys("LIDIA")
        last_name.send_keys("TEST - PHONE")
        phone.send_keys("8055830260")
        self.browser.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        agreement.click()
        submit_button.click()
        time.sleep(4)
        self.assertEqual(self.browser.current_url, f"{self.MAIN_URL}Home/SaveConsumer", 'Formularul nu a fost trimis')

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
