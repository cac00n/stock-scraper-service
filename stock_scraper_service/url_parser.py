from url_info import Currency, BaseUrl, StockMarket


def generate_url(url: BaseUrl, currency: Currency, stock_market: StockMarket) -> str:
    return url.format(currency=currency, stock_market=stock_market)
