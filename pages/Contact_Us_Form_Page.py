import os

from playwright.sync_api import Page


class ContactUsPage:

    def __init__(self, page: Page):

        self.page = page

        self.contact_us_btn = page.locator('[href="/contact_us"]')
        self.get_in_touch_lbl = page.locator('//*[@id="contact-page"]/div[2]/div[1]/div/h2')
        self.name_field = page.locator('[data-qa="name"]')
        self.email_field = page.locator('[data-qa="email"]')
        self.subject_field = page.locator('[data-qa="subject"]')
        self.your_message_field = page.locator('[data-qa="message"]')
        self.upload_button = page.locator('[name="upload_file"]')
        self.submit_btn = page.locator('[class="btn btn-primary pull-left submit_form"]')
        self.alert_success_lbl = page.locator('[class="status alert alert-success"]')
        self.home_btn = page.locator('[id="form-section"]')
        self.test_cases_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')

    def click_contact_us_btn(self):
        self.contact_us_btn.click()

    def check_get_in_touch_lbl(self):
        assert self.get_in_touch_lbl.is_visible(), "get in touch lbl is not visible"

    def input_email_field(self, email):
        self.email_field.fill(email)

    def input_name_field(self, name):
        self.name_field.fill(name)

    def upload_file(self):
        #self.upload_button.set_input_files("testfiles\\test1.txt")
        current_working_dir = os.getcwd()
        file_path = os.path.join(current_working_dir, 'testfiles/test1.txt')

        with self.page.expect_file_chooser() as fc_info:
            self.upload_button.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def click_submit_btn(self):
        self.submit_btn.click()

    def check_alert_success_lbl(self):
        assert self.alert_success_lbl.is_visible()

    def click_home_btn(self):
        self.home_btn.click()

    def click_test_cases_btn(self):
        self.test_cases_btn.click()
