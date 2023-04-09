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
        assert self.category_products_sidebar.is_visible(), "category products sidebar is not visible"

    def click_women_category(self):
        self.women_category.click()

    def click_category_products1(self):
        self.category_products1.click()

    def click_men_category(self):
        self.men_category.click()
        self.category_products3.click()

    def click_products_button(self):
        self.products_button.click()

    def check_brands_products(self):
        assert self.brands_products.is_visible(), "brands products is not visible"

    def click_brands_products_babyhug(self):
        self.brands_products_babyhug.click()

    def click_brands_products_polo(self):
        self.brands_products_polo.click()

    def click_product_add_to_cart(self):
        self.product_add_to_cart.click()

    def click_product_add_to_cart2(self):
        self.product_add_to_cart2.click()

    def click_product_add_to_cart3(self):
        self.product_add_to_cart3.click()

    def click_login_btn(self):
        self.login_btn.click()

    def click_cart_btn(self):
        self.cart_btn.click()

    def check_product_details(self):
        assert self.product_details.is_visible(), "product details is not visible"

    def check_write_your_review_lbl(self):
        assert self.write_your_review_lbl.is_visible(), "write your review lbl is not visible"

    def input_email_review_field(self, email):
        self.email_review_field.fill(email)

    def input_name_review_field(self, name):
        self.name_review_field.fill(name)

    def input_review_field(self, comment):
        self.name_review_field.fill(comment)

    def click_review_button(self):
        self.review_button.click()
