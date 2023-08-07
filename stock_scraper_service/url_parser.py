from stock_scraper_service.url_info import BaseUrl, Currency, StockMarket


def generate_url(url: BaseUrl, currency: Currency, stock_market: StockMarket) -> str:
    return url.format(currency=currency, stock_market=stock_market)
