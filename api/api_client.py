class ApiClient:
    """
    Client for automationexercise.com's public API.
    IMPORTANT: This API always returns HTTP 200 at the transport level.
    The REAL result status lives inside the JSON body's "responseCode" field
    (200 = success, 400 = bad request, 404 = not found, 405 = method not allowed).
    """

    def __init__(self, request_context, base_url="https://automationexercise.com/api"):
        self.request_context = request_context
        self.base_url = base_url

    def get_products_list(self):
        return self.request_context.get(f"{self.base_url}/productsList")

    def post_products_list(self):
        """Should return responseCode 405 - GET-only endpoint."""
        return self.request_context.post(f"{self.base_url}/productsList")

    def get_brands_list(self):
        return self.request_context.get(f"{self.base_url}/brandsList")

    def put_brands_list(self):
        """Should return responseCode 405 - GET-only endpoint."""
        return self.request_context.put(f"{self.base_url}/brandsList")

    def search_product(self, search_term):
        return self.request_context.post(
            f"{self.base_url}/searchProduct",
            form={"search_product": search_term}
        )

    def search_product_no_param(self):
        """Should return responseCode 400 - missing required parameter."""
        return self.request_context.post(f"{self.base_url}/searchProduct")

    def verify_login(self, email, password):
        return self.request_context.post(
            f"{self.base_url}/verifyLogin",
            form={"email": email, "password": password}
        )
