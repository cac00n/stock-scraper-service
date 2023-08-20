from pydantic import BaseModel

from stock_scraper_service.url_info import BaseUrl, Currency, StockMarket


class ScraperSettings(BaseModel):
    base_url: BaseUrl
    currency: Currency
    stock_market: StockMarket
    stock_value_column_name: str
    decimal_separator: str
    thousands_separator: str
