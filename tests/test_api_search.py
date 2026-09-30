def test_search_product_success(api_client):
    response = api_client.search_product("top")
    data = response.json()
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0


def test_search_product_missing_param(api_client):
    response = api_client.search_product_no_param()
    data = response.json()
    assert data["responseCode"] == 400
