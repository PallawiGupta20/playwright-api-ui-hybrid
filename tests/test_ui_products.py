from pages.products_page import ProductsPage


def test_products_page_shows_items(page):
    products_page = ProductsPage(page)
    products_page.goto()
    assert products_page.get_product_count() > 0


def test_search_returns_matching_products(page):
    products_page = ProductsPage(page)
    products_page.goto()
    products_page.search_for("dress")

    names = products_page.get_all_product_names()
    assert len(names) > 0
    assert any("dress" in name.lower() for name in names)
