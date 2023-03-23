import pytest


from pages.Contact_Us_Form_Page import ContactUsPage
from data.test_data import Data
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={ 'width': 1366, 'height': 768 })
        self.contactus = ContactUsPage(self.page)
        self.page.goto('http://automationexercise.com')

    def test_TestCase6_Contact_Us_Form(self, page, test_setup):
        self.contactus.contact_us_btn_click()
        self.contactus.check_get_in_touch_lbl()
        self.contactus.name_field_input(Data.name)
        self.contactus.email_field_input(Data.email)
        self.contactus.subject_field.fill("qwe")
        self.contactus.your_message_field.fill("asd zxc")
        self.contactus.submit_btn_click()
        page.keyboard.press("Enter")
        self.contactus.check_alert_success_lbl()
        self.contactus.home_btn_click()
        take_screenshot(self.page, "Contact_Us_Form")

    def test_TestCase7_Verify_Test_Cases_Page(self, page, test_setup):
        self.contactus.test_cases_btn_click()
        expect(page).to_have_title('Automation Practice Website for UI Testing - Test Cases')
        take_screenshot(self.page, "Verify_Test_Cases_Page")
