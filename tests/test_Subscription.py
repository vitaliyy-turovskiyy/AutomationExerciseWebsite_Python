import pytest


from pages.Subscription_Page import SubscriptionPage
from data.test_data import Data
from pages.Products_Page import ProductsPage
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.subscription = SubscriptionPage(self.page)
        self.products = ProductsPage(self.page)

    def test_TestCase10_Verify_Subscription_in_home_page(self, test_setup):
        self.subscription.scroll_to_footer_area()
        self.subscription.check_subscription_lbl()
        self.subscription.fill_search_field(Data.email)
        self.subscription.click_search_btn()
        self.subscription.check_success_subscribe_lbl()
        take_screenshot(self.page, "Verify_Subscription_in_home_page")

    def test_TestCase11_Verify_Subscription_in_Cart_page(self, test_setup):
        self.subscription.click_cart_btn()
        self.subscription.scroll_to_footer_area()
        self.subscription.check_subscription_lbl()
        self.subscription.fill_search_field(Data.email)
        self.subscription.click_search_btn()
        self.subscription.check_success_subscribe_lbl()
        take_screenshot(self.page, "Verify_Subscription_in_Cart_page")

    def test_TestCase22_Add_to_cart_from_Recommended_items(self, test_setup):
        self.subscription.scroll_to_footer_area()
        self.subscription.check_recommended_items()
        self.subscription.click_product1_btn()
        self.products.click_view_cart_btn()
        self.subscription.check_product1_field()
        take_screenshot(self.page, "Add_to_cart_from_Recommended_items")

    def test_TestCase25_Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality(self, test_setup):
        self.page.set_viewport_size(viewport_size={'width': 900, 'height': 600})
        self.subscription.scroll_to_footer_area()
        self.subscription.check_subscription_lbl()
        self.subscription.click_arrow_up()
        self.subscription.check_slider_carousel()
        take_screenshot(self.page, "Verify_Scroll_Up_using_Arrow_button_and_Scroll_Down_functionality")

    def test_TestCase26_Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality(self, test_setup):
        self.subscription.scroll_to_footer_area()
        self.subscription.check_subscription_lbl()
        self.subscription.scroll_to_header()
        self.subscription.check_slider_carousel()
        take_screenshot(self.page, "Verify_Scroll_Up_without_Arrow_button_and_Scroll_Down_functionality")
