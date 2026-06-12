


def test_web_table(playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers/")
    headers  = page.locator("thead > tr > th")
    col_num = headers.all_text_contents().index("Price")
    print(col_num)

    rice_row = page.locator("tbody > tr").filter(has_text="Rice")
    rice_price = rice_row.locator("td").nth(col_num).text_content()
    print(rice_price)
    