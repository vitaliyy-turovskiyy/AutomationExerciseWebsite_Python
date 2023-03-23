from playwright.sync_api import Page


class SignupPage:

    def __init__(self, page: Page):

        self.page = page

        self.signup_login_btn = page.locator('a[href="/login"]')
        self.register_login = page.locator('p [href="/login"]')
        self.new_user_signup_lbl = page.locator('//*[@id="form"]/div/div/div[3]/div/h2 ')
        self.name_field = page.locator('[data-qa="signup-name"]')
        self.email_signup = page.locator('[data-qa="signup-email"]')
        self.signup_btn = page.locator('[data-qa="signup-button"]')
        self.enter_account_information_lbl = page.locator("//*[text()='Enter Account Information']")
        self.title_mr = page.locator('[id="id_gender1"]')
        self.password_field = page.locator('[id="password"]')
        self.day_of_birth = page.locator('[id="days"]')
        self.months_of_birth = page.locator('id="months"')
        self.years_of_birth = page.locator('[id="years"]')
        self.newsletter_checkbox = page.locator('[id="newsletter"]')
        self.logged_in_as_user_lbl = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
        self.delete_account_btn = page.locator('[href="/delete_account"]')
        self.delete_account_lbl = page.locator('[data-qa="account-deleted"]')
        self.continue_btn2 = page.locator('[data-qa="continue-button"]')
        self.first_name_field = page.locator('[id="first_name"]')
        self.last_name_field = page.locator('[id="last_name"]')
        self.company_field = page.locator('[id="company"]')
        self.address1_field = page.locator('[id="address1"]')
        self.address2_field = page.locator('[id="address2"]')
        self.country_menu = page.locator('[id="country"]')
        self.state_field = page.locator('[data-qa="state"]')
        self.city_field = page.locator('[data-qa="city"]')
        self.zipcode_field = page.locator('[data-qa="zipcode"]')
        self.mobile_number_field = page.locator('[data-qa="mobile_number"]')
        self.create_account_btn = page.locator('[data-qa="create-account"]')
        self.account_created_lbl = page.locator('[data-qa="account-created"]')
        self.continue_btn = page.locator('[class="btn btn-primary"]')
        self.login_your_account_lbl = page.locator('//*[@id="form"]/div/div/div[1]/div/h2')
        self.login_email_address_field = page.locator('[data-qa="login-email"]')
        self.login_password_field = page.locator('[data-qa="login-password"]')
        self.login_btn = page.locator('[data-qa="login-button"]')
        self.inform_message = page.locator('//*[@id="form"]/div/div/div[1]/div/form/p')
        self.logout_btn = page.locator('[href="/logout"]')
        self.inform_message_signup = page.locator('//*[@id="form"]/div/div/div[3]/div/form/p')

    def signup_login_btn_click(self):
        self.signup_login_btn.click()

    def register_login_click(self):
        self.register_login.click()

    def check_new_user_signup_lbl(self):
        self.new_user_signup_lbl.is_visible()

    def name_input(self, name):
        self.name_field.fill(name)

    def email_signup_input(self, email):
        self.email_signup.fill(email)

    def signup_btn_click(self):
        self.signup_btn.click()

    def check_enter_account_information_lbl(self):
        self.enter_account_information_lbl.is_visible()

    def title_mr_click(self):
        self.title_mr.click()

    def password_field_input(self, password):
        self.password_field.fill(password)

    def day_of_birth_click(self):
        self.day_of_birth.click()
        self.day_of_birth.select_option(value="11")

    def months_of_birth_click(self):
        self.months_of_birth.click()
        self.months_of_birth.select_option(value="May")

    def years_of_birth_click(self):
        self.years_of_birth.click()
        self.years_of_birth.select_option(value="2004")

    def newsletter_checkbox_click(self):
        self.newsletter_checkbox.click()

    def first_name_input(self, firstname):
        self.first_name_field.fill(firstname)

    def last_name_field_input(self, lastname):
        self.last_name_field.fill(lastname)

    def company_field_input(self, company):
        self.company_field.fill(company)

    def address1_field_input(self, address):
        self.address1_field.fill(address)

    def address2_field_input(self, address2):
        self.address2_field.fill(address2)

    def country_menu_choose(self):
        self.country_menu.click()
        self.months_of_birth.select_option(value="New Zealand")

    def state_field_input(self, state):
        self.state_field.fill(state)

    def city_field_input(self, city):
        self.city_field.fill(city)

    def zipcode_field_input(self, zipcode):
        self.zipcode_field.fill(zipcode)

    def mobile_number_field_input(self, mobilenumber):
        self.mobile_number_field.fill(mobilenumber)

    def create_account_btn_click(self):
        self.create_account_btn.click()

    def account_created_lbl_check(self):
        self.account_created_lbl.is_visible()

    def continue_btn_click(self):
        self.continue_btn.click()

    def logged_in_as_user_lbl_check(self):
        self.logged_in_as_user_lbl.is_visible()

    def delete_account_btn_click(self):
        self.delete_account_btn.click()

    def delete_account_lbl_check(self):
        self.delete_account_lbl.is_visible()

    def continue_btn2_click(self):
        self.continue_btn2.click()

    def login_your_account_lbl_check(self):
        self.login_your_account_lbl.is_visible()

    def login_email_address_field_input(self, email2):
        self.login_email_address_field.fill(email2)

    def login_password_field_input(self, password):
        self.login_password_field.fill(password)

    def login_btn_click(self):
        self.login_btn.click()

    def inform_message_lbl(self):
        self.inform_message.is_visible()

    def logout_btn_click(self):
        self.logout_btn.click()

    def inform_message_signup_check(self):
        self.inform_message_signup.is_visible()
