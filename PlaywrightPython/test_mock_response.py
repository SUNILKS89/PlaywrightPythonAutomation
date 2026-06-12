from playwright.sync_api import Page


fake_order_response = {"data":[],"message":"No Orders"}


def intercept_message(mesg):
    mesg.fulfill(json=fake_order_response)

def test_mock_response(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_message)
    page.get_by_placeholder("email@example.com").fill("sunilks89@zohomail.in")
    page.get_by_placeholder("enter your passsword").fill("Kota1989!")
    page.locator("#login").click()
    page.get_by_role("button",name="ORDERS").click()

    order_text = page.locator("div.mt-4.ng-star-inserted").text_content()
    print(order_text)