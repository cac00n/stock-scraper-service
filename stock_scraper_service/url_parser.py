import pandas as pd

from stock_scraper_service.config import UrlScraperSettings


class StockScraper:
    def __init__(self, settings: UrlScraperSettings):
        self.url_settings: UrlScraperSettings = settings
        self.stock_value_column_name: str = "stock_value"
        self.datetime_column_name: str = "time_stamp"

    def scrape_stock_information(self) -> pd.DataFrame:
        stock_values_df: pd.DataFrame = pd.read_html(
            self.generate_url(),
            match=self.url_settings.stock_value_column_name,
            header=0,
            decimal=self.url_settings.decimal_separator,
            thousands=self.url_settings.thousands_separator,
            # ignoring type-hints for the next line since pandas type hints are messed up for dictionary keys (int)
            converters={self.url_settings.datetime_column_name: self._transform_to_datetime_format},  # type: ignore
        )[0]
        stock_values_df = self._clean_currency_values(stock_values_df)
        return stock_values_df

    def _transform_to_datetime_format(self, datetime: str | int) -> pd.Timestamp:
        return pd.to_datetime(str(datetime), format="%d%m%y")

    def generate_url(self) -> str:
        return self.url_settings.base_url.format(
            currency=self.url_settings.currency, stock_market=self.url_settings.stock_market
        )

    def _clean_currency_values(self, stock_values_df: pd.DataFrame) -> pd.DataFrame:
        stock_value_column_name: str = self.url_settings.stock_value_column_name
        datetime_column_name: str = self.url_settings.datetime_column_name
        stock_values_df = stock_values_df.rename(
            columns={
                stock_value_column_name: self.stock_value_column_name,
                datetime_column_name: self.datetime_column_name,
            }
        )
        stock_values_df = stock_values_df.set_index(self.datetime_column_name)
        stock_values_df = stock_values_df[[self.stock_value_column_name]]
        return stock_values_df
