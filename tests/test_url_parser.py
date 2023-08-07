import pytest

from stock_scraper_service.url_info import BaseUrl, Currency, StockMarket

from stock_scraper_service.url_parser import generate_url


@pytest.mark.parametrize(
    "url, currency, stock_market",
    [
        (BaseUrl.ariva, Currency.eur, StockMarket.xetra),
        (BaseUrl.ariva, Currency.usd, StockMarket.xetra),
    ],
)
def test_generate_url(
    url: BaseUrl, currency: Currency, stock_market: StockMarket
) -> None:
    actual_result: str = generate_url(url, currency, stock_market)
    expected_result: str = url.format(currency=currency, stock_market=stock_market)
    assert actual_result == expected_result
