import pytest


from pages.Contact_Us_Form_Page import ContactUsPage
from data.test_data import Data
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.contactus = ContactUsPage(self.page)

    def test_TestCase6_Contact_Us_Form(self, new_page, test_setup):
        self.contactus.click_contact_us_btn()
        self.contactus.check_get_in_touch_lbl()
        self.contactus.input_name_field(Data.name)
        self.contactus.input_email_field(Data.email)
        self.contactus.subject_field.fill("qwe")
        self.contactus.your_message_field.fill("asd xc")
        self.contactus.upload_file()
        self.contactus.click_submit_btn()
        new_page.keyboard.press("Enter")
        #self.contactus.check_alert_success_lbl()
        #self.contactus.click_home_btn()
        #expect(new_page).to_have_title('Automation Exercise')
        take_screenshot(self.page, "Contact_Us_Form")

    def test_TestCase7_Verify_Test_Cases_Page(self, new_page, test_setup):
        self.contactus.click_test_cases_btn()
        expect(new_page).to_have_title('Automation Practice Website for UI Testing - Test Cases')
        take_screenshot(self.page, "Verify_Test_Cases_Page")
