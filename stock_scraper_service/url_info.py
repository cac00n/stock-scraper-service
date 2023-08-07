from enum import Enum


class Currency(str, Enum):
    eur: str = "EUR"
    usd: str = "USD"


class StockMarket(str, Enum):
    frankfurt: str = "1"
    hamburg: str = "2"
    hannover: str = "3"
    munich: str = "4"
    l_and_s: str = "16"
    xetra: str = "45"
    tradegate: str = "131"
    gettex: str = "207"


class BaseUrl(str, Enum):
    ariva: str = (
        "https://www.ariva.de/IE00B4L5Y983/kurse/historische-kurse?go=1&boerse_id={stock_market}&month="
        "&currency={currency}&clean_split=1&clean_payout=1&clean_bezug=1"
    )
