from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}

class API_Base:

    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        login_api_response = api_request_context.post("/api/ecom/auth/login",data={"userEmail":"sunilks89@zohomail.in","userPassword":"Kota1989!"})
        assert login_api_response.ok
        token = login_api_response.json()["token"]
        return token

    def create_order(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        api_response = api_request_context.post("/api/ecom/order/create-order",
                                 data=orders_payload,
                                 headers={"Authorization":token,"Content-Type":"application/json"}
                                 )
        print(api_response.json())
        return api_response.json()["orders"][0]