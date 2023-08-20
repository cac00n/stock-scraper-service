import pandas as pd

from stock_scraper_service.config import UrlScraperSettings
from stock_scraper_service.url_info import BaseUrl, Currency, StockMarket
from stock_scraper_service.url_parser import StockScraper


def test_url_scraper() -> None:
    settings = UrlScraperSettings(
        base_url=BaseUrl.ariva,
        currency=Currency.eur,
        stock_market=StockMarket.xetra,
        datetime_column_name="Datum",
        stock_value_column_name="Schluss",
        decimal_separator=",",
        thousands_separator=".",
    )
    stock_scraper = StockScraper(settings)
    stock_values: pd.DataFrame = stock_scraper.scrape_stock_information()

    assert len(stock_values) >= 1
    assert isinstance(stock_values.index, pd.DatetimeIndex)
    assert stock_values.columns == [stock_scraper.stock_value_column_name]
    assert stock_values[stock_scraper.stock_value_column_name].dtype == float
