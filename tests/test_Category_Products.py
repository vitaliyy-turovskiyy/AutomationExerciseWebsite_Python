import pytest


from pages.Category_Products_Page import CategoryPage
from playwright.sync_api import expect
from pages.Place_Order_Page import OrderPage
from pages.Products_Page import ProductsPage
from pages.Signup_Login_Page import SignupPage
from data.test_data import Data
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={ 'width': 1366, 'height': 768 })
        self.product = CategoryPage(self.page)
        self.order = OrderPage(self.page)
        self.products = ProductsPage(self.page)
        self.signup = SignupPage(self.page)
        self.page.goto('http://automationexercise.com')

    def test_TestCase18_View_Category_Products(self, page, test_setup):
        self.product.check_category_products_sidebar()
        self.product.women_category_click()
        self.product.category_products1_click()
        page.wait_for_timeout(3000)
        expect(self.product.title_text).to_contain_text("Women - Dress Products")
        self.product.men_category_click()
        page.wait_for_timeout(2000)
        expect(self.product.title_text).to_contain_text("Men - Tshirts Products")
        take_screenshot(self.page, "Category_Products")

    def test_TestCase19_View_and_Cart_Brand_Products(self, page, test_setup):
        self.product.products_button_click()
        self.product.check_brands_products()
        self.product.brands_products_babyhug_click()
        expect(self.product.title_text).to_contain_text("Brand - Babyhug Products")
        self.product.brands_products_polo_click()
        expect(self.product.title_text).to_contain_text("Polo")
        take_screenshot(self.page, "Cart_Brand_Products")

    def test_TestCase20_Search_Products_and_Verify_Cart_After_Login(self, page, test_setup):
        self.product.products_button_click()
        page.wait_for_timeout(2500)
        expect(self.product.title_text).to_contain_text("All Products")
        self.products.search_field.fill('Tshirt')
        self.products.search_btn_click()
        self.products.check_search_products_lbl()
        expect(self.product.features_items).to_contain_text("Tshirt")
        self.product.product_add_to_cart_click()
        self.products.continue_shopping_btn_click()
        self.product.product_add_to_cart2_click()
        self.products.continue_shopping_btn_click()
        self.product.product_add_to_cart3_click()
        self.products.view_cart_btn_click()
        expect(self.product.product_details).to_contain_text("Men Tshirt")
        self.product.login_btn_click()
        self.signup.login_email_address_field_input(Data.email3)
        self.signup.login_password_field_input(Data.password)
        self.signup.login_btn_click()
        self.product.cart_btn_click()
        self.product.check_product_details()
        take_screenshot(self.page, "Verify_Cart_After_Login")

    def test_TestCase21_Add_review_on_product(self, page, test_setup):
        self.products.products_btn_click()
        expect(page).to_have_title('Automation Exercise - All Products')
        self.products.view_product_btn_click()
        self.product.check_write_your_review_lbl()
        self.product.email_review_field_input(Data.email)
        self.product.name_review_field_input(Data.name)
        self.product.review_field_input()
        self.product.review_button_click()
        self.product.check_thanks_for_message_lbl()
        take_screenshot(self.page, "Add_review_on_product")
