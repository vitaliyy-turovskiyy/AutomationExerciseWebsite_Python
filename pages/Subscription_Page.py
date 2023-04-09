from playwright.sync_api import Page


class SubscriptionPage:

    def __init__(self, page: Page):

        self.page = page

        self.footer_area = page.locator('footer [class="pull-left"]')
        self.subscription_lbl = page.locator("//*[text()='Subscription']")
        self.search_field = page.locator('[id="susbscribe_email"]')
        self.search_btn = page.locator('[class="btn btn-default"]')
        self.success_subscribe_lbl = page.locator('[id="success-subscribe"]')
        self.cart_btn = page.locator('li [href="/view_cart"]')
        self.cart_btn = page.locator('[class="pull-left"]')
        self.recommended_items = page.locator('[class="recommended_items"]')
        self.product1_btn = page.locator('[data-product-id="1"]').last
        self.product1_field = page.locator('[id="product-1"]')
        self.arrow_up = page.locator('[class="fa fa-angle-up"]')
        self.slider_carousel = page.locator('[id="slider-carousel"]')
        self.header = page.locator('[id="header"]')

    def scroll_to_footer_area(self):
        self.footer_area.scroll_into_view_if_needed()

    def check_subscription_lbl(self):
        assert self.subscription_lbl.is_visible(), "subscription lbl is not visible"

    def fill_search_field(self, email):
        self.search_field.fill(email)

    def click_search_btn(self):
        self.search_btn.click()

    def check_success_subscribe_lbl(self):
        assert self.success_subscribe_lbl.is_visible(), "success subscribe lbl is not visible"

    def click_cart_btn(self):
        self.cart_btn.click()

    def check_recommended_items(self):
        assert self.recommended_items.is_visible(), "recommended items is not visible"

    def click_product1_btn(self):
        self.product1_btn.click()

    def check_product1_field(self):
        assert self.product1_field.is_visible(), "product1 field is not visible"

    def click_arrow_up(self):
        self.arrow_up.click()

    def check_slider_carousel(self):
        assert self.slider_carousel.is_visible(), "slider carousel is not visible"

    def scroll_to_header(self):
        self.header.scroll_into_view_if_needed()
