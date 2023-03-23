from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):

        self.page = page

        self.products_btn = page.locator('[href="/products"]')
        self.products_list = page.locator('[class="features_items"]')
        self.view_product_btn = page.locator('[href="/product_details/1"]')
        self.product_name_lbl = page.locator("//*[text()='Blue Top']")
        self.category_lbl = page.locator("//*[text()='Category: Women > Tops']")
        self.price_lbl = page.locator("//span[text()='Rs. 500']")
        self.availability_lbl = page.locator("//*[text()=' In Stock']")
        self.condition_lbl = page.locator("//*[text()=' New']")
        self.brand_lbl = page.locator("//*[text()=' Polo']")
        self.search_field = page.locator('[id="search_product"]')
        self.search_btn = page.locator('[id="submit_search"]')
        self.search_products_lbl = page.locator('[class="title text-center"]')
        self.products_related_lbl = page.locator('[class="features_items"]')
        self.first_product_img = page.locator('[src="/get_product_picture/1"]')
        self.add_to_cart_btn = page.locator('[data-product-id="1"]').first
        self.continue_shopping_btn = page.locator('[class="btn btn-success close-modal btn-block"]')
        self.second_product_img = page.locator('[src="/get_product_picture/2"]')
        self.product_information = page.locator('[class="product-information"]')
        self.product_quantity = page.locator('[id="quantity"]')
        self.add_to_cart_button = page.locator('[class="btn btn-default cart"]')
        self.view_cart_btn = page.locator('p [href="/view_cart"]')
        self.quantity_field = page.locator('[class="disabled"]')
        self.cart_quantity_delete_btn = page.locator('[class="cart_quantity_delete"]')
        self.empty_cart_lbl = page.locator('[id="empty_cart"]')

    def products_btn_click(self):
        self.products_btn.click()

    def check_products_list(self):
        self.products_list.is_visible()

    def view_product_btn_click(self):
        self.view_product_btn.click()

    def check_product_name_lbl(self):
        self.product_name_lbl.is_visible()

    def check_category_lbl(self):
        self.category_lbl.is_visible()

    def check_price_lbl(self):
        self.price_lbl.is_visible()

    def check_availability_lbl(self):
        self.availability_lbl.is_visible()

    def check_condition_lbl(self):
        self.condition_lbl.is_visible()

    def check_brand_lbl(self):
        self.brand_lbl.is_visible()

    def search_btn_click(self):
        self.search_btn.click()

    def check_search_products_lbl(self):
        self.search_products_lbl.is_visible()

    def check_products_related_lbl(self):
        self.products_related_lbl.is_visible()

    def hover_first_product_img(self):
        self.first_product_img.hover()

    def add_to_cart_btn_click(self):
        self.add_to_cart_btn.click()

    def continue_shopping_btn_click(self):
        self.continue_shopping_btn.click()

    def hover_second_product_img(self):
        self.second_product_img.hover()

    def check_product_information(self):
        self.product_information.is_visible()

    def product_quantity_fill(self):
        self.product_quantity.fill('4')

    def add_to_cart_button_click(self):
        self.add_to_cart_button.click()

    def view_cart_btn_click(self):
        self.view_cart_btn.click()

    def cart_quantity_delete_btn_click(self):
        self.cart_quantity_delete_btn.click()
