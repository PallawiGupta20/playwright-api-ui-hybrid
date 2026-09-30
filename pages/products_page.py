from pages.base_page import BasePage


class ProductsPage(BasePage):
    URL = "https://automationexercise.com/products"

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.product_names = page.locator(".productinfo p")

    def goto(self):
        self.page.goto(self.URL)

    def search_for(self, term):
        self.search_input.fill(term)
        self.search_button.click()

    def get_all_product_names(self):
        return self.product_names.all_text_contents()

    def get_product_count(self):
        return self.product_names.count()
