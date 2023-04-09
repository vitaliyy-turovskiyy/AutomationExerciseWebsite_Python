from playwright.sync_api import Page


class OrderPage:

    def __init__(self, page: Page):

        self.page = page

        self.add_to_card1 = page.locator('//*[@src="/get_product_picture/1"]/../a')
        self.view_cart_btn = page.locator('p [href="/view_cart"]')
        self.check_out_btn = page.locator('[class="btn btn-default check_out"]')
        self.register_login_btn = page.locator('p [href="/login"]')
        self.view_cart_button = page.locator('li [href="/view_cart"]')
        self.address_delivery_field = page.locator('[id="address_delivery"]')
        self.address_billing_field = page.locator('[id="address_invoice"]')
        self.form_control_field = page.locator('[class="form-control"]')
        self.place_order_btn = page.locator('[class="btn btn-default check_out"]')
        self.name_on_card = page.locator('[data-qa="name-on-card"]')
        self.card_number = page.locator('[data-qa="card-number"]')
        self.cvc_number = page.locator('[data-qa="cvc"]')
        self.expiry_month = page.locator('[data-qa="expiry-month"]')
        self.expiry_year = page.locator('[data-qa="expiry-year"]')
        self.pay_button = page.locator('[data-qa="pay-button"]')
        self.success_message = page.locator('[style="font-size: 20px; font-family: garamond;"]')
        self.download_invoice_btn = page.locator('[class="btn btn-default check_out"]')

    def click_add_to_card1(self):
        self.add_to_card1.click()

    def click_view_cart_btn(self):
        self.view_cart_btn.click()

    def check_out_btn_click(self):
        self.check_out_btn.click()

    def click_register_login_btn(self):
        self.register_login_btn.click()

    def click_view_cart_button(self):
        self.view_cart_button.click()

    def fill_form_control_field(self, sometext):
        self.form_control_field.fill(sometext)

    def click_place_order_btn(self):
        self.place_order_btn.click()

    def fill_name_on_card(self, NameonCard):
        self.name_on_card.fill(NameonCard)

    def fill_card_number(self, CardNumber):
        self.card_number.fill(CardNumber)

    def fill_cvc_number(self, CVC):
        self.cvc_number.fill(CVC)

    def fill_expiry_month(self, Expiration):
        self.expiry_month.fill(Expiration)

    def fill_expiry_year(self, date):
        self.expiry_year.fill(date)

    def click_pay_button(self):
        self.pay_button.click()

    def check_success_message(self):
        assert self.success_message.is_visible(), "success message is not visible"

    def click_download_invoice_btn(self):
        self.download_invoice_btn.click()
