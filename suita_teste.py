import unittest

from test_open_form import OpenPage
from test_displayed_messages import DisplayedMessages
from test_links import AccessLinks
from test_submit_address import SubmitFormAddress
from test_submit_email import SubmitFormEmail
from test_submit_phone import SubmitFormPhone


from html_test_runner import HTMLTestRunner
import HTMLTestRunner


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(OpenPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(DisplayedMessages),
            unittest.defaultTestLoader.loadTestsFromTestCase(SubmitFormAddress),
            unittest.defaultTestLoader.loadTestsFromTestCase(SubmitFormEmail),
            unittest.defaultTestLoader.loadTestsFromTestCase(SubmitFormPhone),
            unittest.defaultTestLoader.loadTestsFromTestCase(AccessLinks)
        ])
        runner = HTMLTestRunner.HTMLTestRunner(combine_reports=True, report_title="Functioning testing",
                                               report_name="Sumar teste")

        runner.run(tests_to_run)
