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
        self.upload_file_field = page.locator('[name="upload_file"]')
        self.submit_btn = page.locator('[data-qa="submit-button"]')
        self.alert_success_lbl = page.locator('[class="status alert alert-success"]')
        self.home_btn = page.locator('[id="form-section"]')
        self.test_cases_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')

    def contact_us_btn_click(self):
        self.contact_us_btn.click()

    def check_get_in_touch_lbl(self):
        self.get_in_touch_lbl.is_visible()

    def email_field_input(self, email):
        self.email_field.fill(email)

    def name_field_input(self, name):
        self.name_field.fill(name)

    def submit_btn_click(self):
        self.submit_btn.click()

    def check_alert_success_lbl(self):
        self.alert_success_lbl.is_visible()

    def home_btn_click(self):
        self.home_btn.click()

    def test_cases_btn_click(self):
        self.test_cases_btn.click()
