import pytest
from playwright.sync_api import Page, expect

def test_currency_conversion_flow(page: Page):
    page.goto("https://www.xe.com/currencyconverter/")
    
    # Cookie və ya reklam çıxsa bağlayır
    if page.get_by_role("button", name="Accept").is_visible():
        page.get_by_role("button", name="Accept").click()

    # 100 USD -> AZN çevrilməsini yoxlayır
    page.locator("#amount").fill("100")
    page.locator("#midmarketFromCurrency-wrapper input").fill("USD")
    page.keyboard.press("Enter")
    page.locator("#midmarketToCurrency-wrapper input").fill("AZN")
    page.keyboard.press("Enter")

    page.get_by_role("button", name="Convert").click()
    
    # Nəticənin göründüyünü təsdiqləyirik
    expect(page.locator("p[class*='result__BigRate']")).to_be_visible()
