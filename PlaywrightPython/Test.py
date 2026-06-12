from playwright.sync_api import sync_playwright
import pytest
import time
from playwright.sync_api import expect
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://playwright.dev")
#     print("Page Title:", page.title())
#     browser.close()

#@pytest.mark.skip
def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev")
    page.close()

@pytest.mark.skip
def test_playwright_shortcut(page):
    page.goto("https://playwright.dev")


@pytest.mark.skip
def test_login_page(playwright):    
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    time.sleep(5)

@pytest.mark.skip
def test_UI(playwright):    
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()

    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()

    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()

    page.get_by_text("Checkout").click()

    expect(page.locator("div.media > div.media-body")).to_have_count(2)
    time.sleep(5)

def test_childwindowHandle(playwright):
    browser = playwright.chromium.launch(headless=False)
    page =browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")  
    with page.expect_popup() as newpage_info:
        page.locator("div > a.blinkingText:nth-child(1)").click()
        child_page = newpage_info.value
        text  = child_page.locator("div > p.im-para.red").text_content()
        print(text)
        words = text.split("at")
        print(words[0])
        print(words[1])
        fetch_email = words[1].strip().split(" ")#used strip() to remove space at the start 
        print(fetch_email[0])
        email = fetch_email[0]
        assert email == "mentor@rahulshettyacademy.com"