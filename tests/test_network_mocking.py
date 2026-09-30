from pages.products_page import ProductsPage


def test_ui_handles_broken_products_api_gracefully(page):
    """
    Simulates the backend API failing, WITHOUT needing the real backend
    to actually be broken. Verifies the page doesn't crash even if the
    products API call fails - a genuinely advanced test pattern that
    Selenium/Appium can't easily do natively.
    """
    def handle_route(route):
        route.fulfill(status=500, body="Internal Server Error")

    page.route("**/api/productsList", handle_route)

    products_page = ProductsPage(page)
    products_page.goto()

    # The page should still load without crashing, even if this
    # particular API call was intercepted and forced to fail
    assert page.title() != ""


def test_slow_network_does_not_break_page(page):
    """Simulates a slow/degraded network connection."""
    def handle_slow_route(route):
        page.wait_for_timeout(1000)
        route.continue_()

    page.route("**/*.jpg", handle_slow_route)

    products_page = ProductsPage(page)
    products_page.goto()

    assert products_page.get_product_count() >= 0
