from playwright.sync_api import Page


class CategoryPage:

    def __init__(self, page: Page):

        self.page = page

        self.category_products_sidebar = page.locator('[class="panel-group category-products"]')
        self.women_category = page.locator('[href="#Women"]')
        self.category_products1 = page.locator('[href="/category_products/1"]')
        self.title_text = page.locator('[class="title text-center"]')
        self.men_category = page.locator('[href="#Men"]')
        self.category_products3 = page.locator('[href="/category_products/3"]')
        self.products_button = page.locator('[href="/products"]')
        self.brands_products = page.locator('[class="brands_products"]')
        self.brands_products_babyhug = page.locator('[href="/brand_products/Babyhug"]')
        self.brands_products_polo = page.locator('[href="/brand_products/Polo"]')
        self.features_items = page.locator('[class="features_items"]')
        self.product_add_to_cart = page.locator('[data-product-id="2"]').first
        self.product_add_to_cart2 = page.locator('[data-product-id="28"]').first
        self.product_add_to_cart3 = page.locator('[data-product-id="29"]').first
        self.product_details = page.locator('[href="/product_details/2"]')
        self.login_btn = page.locator('li [href="/login"]')
        self.cart_btn = page.locator('li [href="/view_cart"]')
        self.write_your_review_lbl = page.locator('[class="active"]')
        self.name_review_field = page.locator('[id="name"]')
        self.email_review_field = page.locator('[id="email"]')
        self.review_field = page.locator('[id="review"]')
        self.review_button = page.locator('[id="button-review"]')
        self.thanks_for_message_lbl = page.locator('[style="font-size: 20px;"]')

    def check_category_products_sidebar(self):
        self.category_products_sidebar.is_visible()

    def women_category_click(self):
        self.women_category.click()

    def category_products1_click(self):
        self.category_products1.click()

    def men_category_click(self):
        self.men_category.click()
        self.category_products3.click()

    def products_button_click(self):
        self.products_button.click()

    def check_brands_products(self):
        self.brands_products.is_visible()

    def brands_products_babyhug_click(self):
        self.brands_products_babyhug.click()

    def brands_products_polo_click(self):
        self.brands_products_polo.click()

    def product_add_to_cart_click(self):
        self.product_add_to_cart.click()

    def product_add_to_cart2_click(self):
        self.product_add_to_cart2.click()

    def product_add_to_cart3_click(self):
        self.product_add_to_cart3.click()

    def login_btn_click(self):
        self.login_btn.click()

    def cart_btn_click(self):
        self.cart_btn.click()

    def check_product_details(self):
        self.product_details.is_visible()

    def check_write_your_review_lbl(self):
        self.write_your_review_lbl.is_visible()

    def email_review_field_input(self, email):
        self.email_review_field.fill(email)

    def name_review_field_input(self, name):
        self.name_review_field.fill(name)

    def review_field_input(self):
        self.name_review_field.fill("Nice top")

    def review_button_click(self):
        self.review_button.click()

    def check_thanks_for_message_lbl(self):
        self.thanks_for_message_lbl.is_visible()
