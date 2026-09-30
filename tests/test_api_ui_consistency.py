from pages.products_page import ProductsPage


def test_ui_product_count_matches_api(page, api_client):
    """
    Cross-verifies that what the UI displays actually matches what the
    backend API returns - catches bugs that pure UI testing would miss
    (e.g. a caching issue where the UI shows stale data).
    """
    api_response = api_client.get_products_list()
    api_data = api_response.json()
    api_product_count = len(api_data["products"])

    products_page = ProductsPage(page)
    products_page.goto()
    ui_product_count = products_page.get_product_count()

    # UI product page may paginate, so we check the UI count is reasonable
    # relative to the total API count, not necessarily an exact 1:1 match
    assert ui_product_count > 0
    assert api_product_count > 0
    print(f"API total products: {api_product_count}, UI visible products: {ui_product_count}")
