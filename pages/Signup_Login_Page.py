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
        self.months_of_birth = page.locator('[id="months"]')
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

    def click_signup_login_btn(self):
        self.signup_login_btn.click()

    def click_register_login(self):
        self.register_login.click()

    def check_new_user_signup_lbl(self):
        assert self.new_user_signup_lbl.is_visible(), "new user signup lbl is not visible"

    def input_name(self, name):
        self.name_field.fill(name)

    def input_email_signup(self, email):
        self.email_signup.fill(email)

    def click_signup_btn(self):
        self.signup_btn.click()

    def check_enter_account_information_lbl(self):
        assert self.enter_account_information_lbl.is_visible(), "enter account information lbl is not visible"

    def click_title_mr(self):
        self.title_mr.click()

    def input_password_field(self, password):
        self.password_field.fill(password)

    def click_day_of_birth(self, day):
        self.day_of_birth.click()
        self.day_of_birth.select_option(value=day)

    def months_of_birth_click(self, months):
        self.months_of_birth.click()
        self.months_of_birth.select_option(value=months)

    def years_of_birth_click(self, years):
        self.years_of_birth.click()
        self.years_of_birth.select_option(value=years)

    def click_newsletter_checkbox(self):
        self.newsletter_checkbox.click()

    def input_first_name(self, firstname):
        self.first_name_field.fill(firstname)

    def input_last_name_field(self, lastname):
        self.last_name_field.fill(lastname)

    def input_company_to_field(self, company):
        self.company_field.fill(company)

    def input_address1_to_field(self, address):
        self.address1_field.fill(address)

    def input_address2_to_field(self, address2):
        self.address2_field.fill(address2)

    def country_menu_choose(self, country):
        self.country_menu.click()
        self.country_menu.select_option(value=country)

    def input_state_to_field(self, state):
        self.state_field.fill(state)

    def input_city_to_field(self, city):
        self.city_field.fill(city)

    def input_zipcode_to_field(self, zipcode):
        self.zipcode_field.fill(zipcode)

    def input_mobile_number(self, mobilenumber):
        self.mobile_number_field.fill(mobilenumber)

    def click_create_account_btn(self):
        self.create_account_btn.click()

    def check_account_created_lbl(self):
        assert self.account_created_lbl.is_visible(), "account created lbl is not visible"

    def click_continue_btn(self):
        self.continue_btn.click()

    def check_logged_in_as_user_lbl(self):
        assert self.logged_in_as_user_lbl.is_visible(), "logged_in as user lbl is not visible"

    def click_delete_account_btn(self):
        self.delete_account_btn.click()

    def check_delete_account_lbl(self):
        assert self.delete_account_lbl.is_visible(), "delete account lbl is not visible()"

    def click_continue_btn2(self):
        self.continue_btn2.click()

    def check_login_your_account_lbl(self):
        assert self.login_your_account_lbl.is_visible(), "login your account lbl is not visible"

    def input_login_email_address_to_field(self, email2):
        self.login_email_address_field.fill(email2)

    def input_login_password_to_field(self, password):
        self.login_password_field.fill(password)

    def click_login_btn(self):
        self.login_btn.click()

    def check_inform_message_lbl(self):
        assert self.inform_message.is_visible(), "inform message is not visible"

    def click_logout_btn(self):
        self.logout_btn.click()

    def check_inform_message_signup(self):
        assert self.inform_message_signup.is_visible(), "inform message:Email Address already exist! is not visible()"
