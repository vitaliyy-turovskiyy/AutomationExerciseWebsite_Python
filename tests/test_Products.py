import pytest


from pages.Products_Page import ProductsPage
from playwright.sync_api import expect
from pages.Place_Order_Page import OrderPage
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={ 'width': 1366, 'height': 768 })
        self.products = ProductsPage(self.page)
        self.order = OrderPage(self.page)
        self.page.goto('http://automationexercise.com')

    def test_TestCase8_Verify_All_Products_and_product_detail_page(self, page, test_setup):
        self.products.products_btn_click()
        expect(page).to_have_url('https://automationexercise.com/products')
        self.products.check_products_list()
        self.products.view_product_btn_click()
        expect(page).to_have_url('https://automationexercise.com/product_details/1')
        self.products.check_product_name_lbl()
        self.products.check_category_lbl()
        self.products.check_price_lbl()
        self.products.check_availability_lbl()
        self.products.check_brand_lbl()
        take_screenshot(self.page, "Verify_All_Products_and_product_detail_page")

    def test_TestCase9_Search_Product(self, page, test_setup):
        self.products.products_btn_click()
        expect(page).not_to_have_title('Automation Exercise - All Product')
        self.products.search_field.fill('Tshirt')
        self.products.search_btn_click()
        self.products.check_search_products_lbl()
        self.products.check_products_related_lbl()
        take_screenshot(self.page, "Search_Product")

    def test_TestCase12_Add_Products_in_Cart(self, page, test_setup):
        self.products.products_btn_click()
        self.products.hover_first_product_img()
        page.wait_for_timeout(2000)
        self.products.add_to_cart_btn_click()
        page.wait_for_timeout(2000)
        self.products.continue_shopping_btn_click()
        self.products.hover_second_product_img()
        take_screenshot(self.page, "Add_Products_in_Cart")

    def test_TestCase13_Verify_Product_quantity_in_Cart(self, page, test_setup):
        self.products.view_product_btn_click()
        self.products.check_product_information()
        self.products.product_quantity_fill()
        self.products.add_to_cart_button_click()
        self.products.view_cart_btn_click()
        expect(self.products.quantity_field).to_contain_text("4")
        take_screenshot(self.page, "Verify_Product_quantity_in_Cart")

    def test_TestCase17_Remove_Products_From_Cart(self, page, test_setup):
        self.order.add_to_card1_click()
        self.order.view_cart_btn_click()
        expect(page).to_have_url('https://automationexercise.com/view_cart')
        self.products.cart_quantity_delete_btn_click()
        expect(self.products.empty_cart_lbl).to_contain_text("Cart is empty!")
        take_screenshot(self.page, "Remove_Products_From_Cart")
