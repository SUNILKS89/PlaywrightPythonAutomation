from playwright.sync_api import expect
import pytest
import time


@pytest.mark.skip
def test_UI_Tests(playwright):
    browser = playwright.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    #element = page.get_by_role("button",name="Hide")
    element = page.locator("#hide-textbox")
    element.scroll_into_view_if_needed()
    element.click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()    


def test_alert_window(playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #alert window handling
    page.on("dialog", lambda dialog:dialog.accept())
    #element = page.get_by_role("button", name="Confirm")
    element = page.locator("#confirmbtn")
    element.scroll_into_view_if_needed()
    element.click()
    time.sleep(4)    

    #frame handling with palywright
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link",name="All Access plan").click()
    
def test_MouseHovering(playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()