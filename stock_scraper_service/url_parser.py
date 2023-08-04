import pandas as pd
from url_info import Currency, BaseUrl, StockMarket


def generate_url(url: BaseUrl, currency: Currency, stock_market: StockMarket) -> str:
    return url.format(currency=currency, stock_market=stock_market)


# table_identifier: str = "Schluss"
# table_index: int = 0
#
# df: pd.DataFrame = pd.read_html(
#     get_url(Currency.EUR),
#     match=table_identifier,
#     index_col=table_index,
#     header=0,
#     parse_dates=True,
# )[0]
#
# df = df[["Schluss"]]
# df["Schluss"] = df["Schluss"].str.extract(r'(^\d*[.,]?\d*)')
# df["Schluss"] = df["Schluss"].str.replace(",", ".").astype(float)
# print(df)



