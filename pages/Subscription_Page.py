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

    def footer_area_scroll(self):
        self.footer_area.scroll_into_view_if_needed()

    def check_subscription_lbl(self):
        self.subscription_lbl.is_visible()

    def search_field_fill(self, email):
        self.search_field.fill(email)

    def search_btn_click(self):
        self.search_btn.click()

    def check_success_subscribe_lbl(self):
        self.success_subscribe_lbl.is_visible()

    def cart_btn_click(self):
        self.cart_btn.click()

    def check_recommended_items(self):
        self.recommended_items.is_visible()

    def product1_btn_click(self):
        self.product1_btn.click()

    def check_product1_field(self):
        self.product1_field.is_visible()

    def arrow_up_click(self):
        self.arrow_up.click()

    def check_slider_carousel(self):
        self.slider_carousel.is_visible()

    def scroll_to_header(self):
        self.header.scroll_into_view_if_needed()
