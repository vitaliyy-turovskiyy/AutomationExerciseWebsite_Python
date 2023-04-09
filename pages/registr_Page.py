from playwright.sync_api import Page


class RegistrPage:

    def __init__(self, page: Page):

        self.page = page

        self.title_mr = page.locator('[id="id_gender1"]')
        self.password_field = page.locator('[id="password"]')
        self.day_of_birth = page.locator('[id="days"]')
        self.months_of_birth = page.locator('[id="months"]')
        self.years_of_birth = page.locator('[id="years"]')
        self.newsletter_checkbox = page.locator('[id="newsletter"]')
        self.first_name_field = page.locator('[id="first_name"]')
        self.last_name_field = page.locator('[id="last_name"]')
        self.company_field = page.locator('[id="company"]')
        self.address1_field = page.locator('[id="address1"]')
        self.address2_field = page.locator('[id="address2"]')
        self.country_menu = page.locator('[id="country"]')
        self.state_field = page.locator('[data-qa="state"]')
        self.city_field = page.locator('[data-qa="city"]')
        self.zipcode_field = page.locator('[data-qa="zipcode"]')
        self.mobile_number_field = page.locator('[data-qa="mobile_number"]')
        self.create_account_btn = page.locator('[data-qa="create-account"]')

    def fill_registration_form(self, password, day, months, years, firstname, lastname, company, address, address2, country, state, city, zipcode, mobilenumber ):
        self.title_mr.click()
        self.password_field.fill(password)
        self.day_of_birth.click()
        self.day_of_birth.select_option(value=day)
        self.months_of_birth.click()
        self.months_of_birth.select_option(value=months)
        self.years_of_birth.click()
        self.years_of_birth.select_option(value=years)
        self.newsletter_checkbox.click()
        self.first_name_field.fill(firstname)
        self.last_name_field.fill(lastname)
        self.company_field.fill(company)
        self.address1_field.fill(address)
        self.address2_field.fill(address2)
        self.country_menu.click()
        self.country_menu.select_option(value=country)
        self.state_field.fill(state)
        self.city_field.fill(city)
        self.zipcode_field.fill(zipcode)
        self.mobile_number_field.fill(mobilenumber)
        self.create_account_btn.click()
