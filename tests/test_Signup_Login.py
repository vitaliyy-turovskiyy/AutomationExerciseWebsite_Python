import pytest


from pages.Signup_Login_Page import SignupPage
from data.test_data import Data
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestSignup:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={ 'width': 1366, 'height': 768 })
        self.signup = SignupPage(self.page)
        self.page.goto('http://automationexercise.com')

    def test_TestCase1_Register_User(self, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.check_new_user_signup_lbl()
        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email)
        self.signup.signup_btn_click()
        self.signup.check_enter_account_information_lbl()
        self.signup.title_mr_click()
        self.signup.password_field_input(Data.password)
        self.signup.day_of_birth_click()
        self.signup.newsletter_checkbox_click()
        self.signup.first_name_input(Data.firstname)
        self.signup.last_name_field_input(Data.lastname)
        self.signup.company_field_input(Data.company)
        self.signup.address1_field_input(Data.address)
        self.signup.address2_field_input(Data.address2)
        self.signup.state_field_input(Data.state)
        self.signup.city_field_input(Data.city)
        self.signup.zipcode_field_input(Data.zipcode)
        self.signup.mobile_number_field_input(Data.mobilenumber)
        self.signup.create_account_btn_click()
        self.signup.account_created_lbl_check()
        self.signup.continue_btn_click()
        self.signup.logged_in_as_user_lbl_check()
        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        self.signup.continue_btn2_click()
        take_screenshot(self.page, "Register_User")

    def test_TestCase2_Login_User_with_correct_email_and_password(self, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.login_your_account_lbl_check()
        self.signup.login_email_address_field_input(Data.email2)
        self.signup.login_password_field_input(Data.password)
        self.signup.login_btn_click()
        self.signup.logged_in_as_user_lbl_check()
        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        take_screenshot(self.page, "Login_User_with_correct_email_and_password")
        self.signup.signup_login_btn_click()
        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email2)
        self.signup.signup_btn_click()
        self.signup.title_mr_click()
        self.signup.password_field_input(Data.password)
        self.signup.day_of_birth_click()
        self.signup.newsletter_checkbox_click()
        self.signup.first_name_input(Data.firstname)
        self.signup.last_name_field_input(Data.lastname)
        self.signup.company_field_input(Data.company)
        self.signup.address1_field_input(Data.address)
        self.signup.address2_field_input(Data.address2)
        self.signup.state_field_input(Data.state)
        self.signup.city_field_input(Data.city)
        self.signup.zipcode_field_input(Data.zipcode)
        self.signup.mobile_number_field_input(Data.mobilenumber)
        self.signup.create_account_btn_click()

    def test_TestCase3_Login_User_with_incorrect_email_and_password(self, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.login_your_account_lbl_check()
        self.signup.login_email_address_field.fill("sdfaasc@1")
        self.signup.login_password_field_input(Data.password)
        self.signup.login_btn_click()
        self.signup.inform_message_lbl()
        take_screenshot(self.page, "Login_User_with_incorrect_email_and_password")

    def test_TestCase4_Logout_User(self, page, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.login_your_account_lbl_check()
        self.signup.login_email_address_field_input(Data.email3)
        self.signup.login_password_field_input(Data.password)
        self.signup.login_btn_click()
        self.signup.logged_in_as_user_lbl_check()
        self.signup.logout_btn_click()
        expect(page).to_have_title('Automation Exercise - Signup / Login')
        take_screenshot(self.page, "Logout_User")

    def test_Test_Case5_Register_User_with_existing_email(self, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.check_new_user_signup_lbl()
        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email2)
        self.signup.signup_btn_click()
        self.signup.inform_message_signup_check()
        self.signup.logged_in_as_user_lbl_check()
        take_screenshot(self.page, "Register_User_with_existing_email")
