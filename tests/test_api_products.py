def test_get_products_list_success(api_client):
    response = api_client.get_products_list()
    assert response.status == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0
    assert "name" in data["products"][0]


def test_post_products_list_not_allowed(api_client):
    response = api_client.post_products_list()
    data = response.json()
    assert data["responseCode"] == 405


def test_get_brands_list_success(api_client):
    response = api_client.get_brands_list()
    data = response.json()
    assert data["responseCode"] == 200
    assert len(data["brands"]) > 0


def test_put_brands_list_not_allowed(api_client):
    response = api_client.put_brands_list()
    data = response.json()
    assert data["responseCode"] == 405
