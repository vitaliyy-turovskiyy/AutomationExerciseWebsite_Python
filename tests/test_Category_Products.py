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
    def test_setup(self, new_page):
        self.page = new_page
        self.product = CategoryPage(self.page)
        self.order = OrderPage(self.page)
        self.products = ProductsPage(self.page)
        self.signup = SignupPage(self.page)

    def test_TestCase18_View_Category_Products(self, page, test_setup):
        self.product.check_category_products_sidebar()
        self.product.click_women_category()
        self.product.click_category_products1()
        page.wait_for_timeout(3000)
        expect(self.product.title_text).to_contain_text("Women - Dress Products")
        self.product.click_men_category()
        page.wait_for_timeout(2000)
        expect(self.product.title_text).to_contain_text("Men - Tshirts Products")
        take_screenshot(self.page, "Category_Products")

    def test_TestCase19_View_and_Cart_Brand_Products(self, page, test_setup):
        self.product.click_products_button()
        self.product.check_brands_products()
        self.product.click_brands_products_babyhug()
        expect(self.product.title_text).to_contain_text("Brand - Babyhug Products")
        self.product.click_brands_products_polo()
        expect(self.product.title_text).to_contain_text("Polo")
        take_screenshot(self.page, "Cart_Brand_Products")

    def test_TestCase20_Search_Products_and_Verify_Cart_After_Login(self, page, test_setup):
        self.product.click_products_button()
        page.wait_for_timeout(2500)
        expect(self.product.title_text).to_contain_text("All Products")
        self.products.search_field.fill('Tshirt')
        self.products.click_search_btn()
        self.products.check_search_products_lbl()
        expect(self.product.features_items).to_contain_text("Tshirt")
        self.product.click_product_add_to_cart()
        self.products.click_continue_shopping_btn()
        self.product.click_product_add_to_cart2()
        self.products.click_continue_shopping_btn()
        self.product.click_product_add_to_cart3()
        self.products.click_view_cart_btn()
        expect(self.product.product_details).to_contain_text("Men Tshirt")
        self.product.click_login_btn()
        self.signup.input_login_email_address_to_field(Data.email3)
        self.signup.input_login_password_to_field(Data.password)
        self.signup.click_login_btn()
        self.product.click_cart_btn()
        self.product.check_product_details()
        take_screenshot(self.page, "Verify_Cart_After_Login")

    def test_TestCase21_Add_review_on_product(self, new_page, test_setup):
        self.products.click_products_btn()
        expect(new_page).to_have_title('Automation Exercise - All Products')
        self.products.click_view_product_btn()
        self.product.check_write_your_review_lbl()
        self.product.input_email_review_field(Data.email)
        self.product.input_name_review_field(Data.name)
        self.product.input_review_field(Data.comment)
        self.product.click_review_button()
        expect(self.product.thanks_for_message_lbl).to_contain_text("Thank you for your review.")
        take_screenshot(self.page, "Add_review_on_product")
