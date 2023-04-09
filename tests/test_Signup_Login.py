import pytest


from pages.Signup_Login_Page import SignupPage
from pages.registr_Page import RegistrPage
from data.test_data import Data
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestSignup:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.signup = SignupPage(self.page)
        self.registr = RegistrPage(self.page)

    def test_TestCase1_Register_User(self, test_setup):
        self.signup.click_signup_login_btn()
        self.signup.check_new_user_signup_lbl()
        self.signup.input_name(Data.name)
        self.signup.input_email_signup(Data.email)
        self.signup.click_signup_btn()
        self.signup.check_enter_account_information_lbl()
        self.registr.fill_registration_form(Data.password, Data.day, Data.months, Data.years, Data.firstname, Data.lastname, Data.company, Data.address, Data.address2,Data.country, Data.state, Data.city, Data.zipcode, Data.mobilenumber)
        self.signup.check_account_created_lbl()
        self.signup.click_continue_btn()
        self.signup.check_logged_in_as_user_lbl()
        self.signup.click_delete_account_btn()
        self.signup.check_delete_account_lbl()
        self.signup.click_continue_btn2()
        take_screenshot(self.page, "Register_User")

    def test_TestCase2_Login_User_with_correct_email_and_password(self, test_setup):
        self.signup.click_signup_login_btn()
        self.signup.check_login_your_account_lbl()
        self.signup.input_login_email_address_to_field(Data.email2)
        self.signup.input_login_password_to_field(Data.password)
        self.signup.click_login_btn()
        self.signup.check_logged_in_as_user_lbl()
        self.signup.click_delete_account_btn()
        self.signup.check_delete_account_lbl()
        take_screenshot(self.page, "Login_User_with_correct_email_and_password")
        self.signup.click_signup_login_btn()
        self.signup.input_name(Data.name)
        self.signup.input_email_signup(Data.email2)
        self.signup.click_signup_btn()
        self.registr.fill_registration_form(Data.password, Data.day, Data.months, Data.years, Data.firstname,Data.lastname, Data.company, Data.address, Data.address2, Data.country,Data.state, Data.city, Data.zipcode, Data.mobilenumber)

    def test_TestCase3_Login_User_with_incorrect_email_and_password(self, test_setup):
        self.signup.click_signup_login_btn()
        self.signup.check_login_your_account_lbl()
        self.signup.login_email_address_field.fill("sdfaasc@1")
        self.signup.input_login_password_to_field(Data.password)
        self.signup.click_login_btn()
        self.signup.check_inform_message_lbl()
        take_screenshot(self.page, "Login_User_with_incorrect_email_and_password")

    def test_TestCase4_Logout_User(self, new_page, test_setup):
        self.signup.click_signup_login_btn()
        self.signup.check_login_your_account_lbl()
        self.signup.input_login_email_address_to_field(Data.email3)
        self.signup.input_login_password_to_field(Data.password)
        self.signup.click_login_btn()
        self.signup.check_logged_in_as_user_lbl()
        self.signup.click_logout_btn()
        expect(new_page).to_have_title('Automation Exercise - Signup / Login')
        take_screenshot(self.page, "Logout_User")

    def test_Test_Case5_Register_User_with_existing_email(self, test_setup):
        self.signup.click_signup_login_btn()
        self.signup.check_new_user_signup_lbl()
        self.signup.input_name(Data.name)
        self.signup.input_email_signup(Data.email2)
        self.signup.click_signup_btn()
        self.signup.check_inform_message_signup()
        self.signup.check_logged_in_as_user_lbl()
        take_screenshot(self.page, "Register_User_with_existing_email")
