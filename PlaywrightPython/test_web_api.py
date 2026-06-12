from playwright.sync_api import Playwright,expect
import time
from Utils.apiBase import *

def test_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    #API call for creating order
    api_base= API_Base()
    order_id = api_base.create_order(playwright)

    #login through GUI
    page.get_by_placeholder("email@example.com").fill("sunilks89@zohomail.in")
    page.get_by_placeholder("enter your passsword").fill("Kota1989!")
    page.locator("#login").click()

    page.get_by_role("button",name="ORDERS").click()

    order_row = page.locator("tbody > tr").filter(has_text=order_id)
    order_row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    time.sleep(5)
