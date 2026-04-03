import pytest
from playwright.sync_api import Playwright

def test_exchange_rate_data_integrity(playwright: Playwright):
    api_request_context = playwright.request.new_context(base_url="https://open.er-api.com")
    response = api_request_context.get("/v6/latest/USD")
    
    assert response.status == 200
    data = response.json()
    
    # Məzənnənin doğruluğunu və AZN-in mövcudluğunu yoxlayırıq
    assert data["result"] == "success"
    assert "AZN" in data["rates"]
    assert data["rates"]["AZN"] > 0
    
    api_request_context.dispose()
