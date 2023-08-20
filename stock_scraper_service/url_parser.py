import pandas as pd

from stock_scraper_service.config import ScraperSettings


class StockScraper:
    def __init__(self, settings: ScraperSettings):
        self.settings: ScraperSettings = settings
        self.stock_value_column_name: str = "stock_value"

    def scrape_stock_information(self) -> pd.DataFrame:
        stock_values_df: pd.DataFrame = pd.read_html(
            self.generate_url(),
            match=self.settings.stock_value_column_name,
            index_col=0,
            header=0,
            parse_dates=True,
            decimal=self.settings.decimal_separator,
            thousands=self.settings.thousands_separator,
        )[0]
        stock_values_df = self._clean_currency_values(stock_values_df)
        return stock_values_df

    def generate_url(self) -> str:
        return self.settings.base_url.format(currency=self.settings.currency, stock_market=self.settings.stock_market)

    def _clean_currency_values(self, stock_values_df: pd.DataFrame) -> pd.DataFrame:
        stock_value_column_name: str = self.settings.stock_value_column_name
        stock_values_df = stock_values_df[[stock_value_column_name]]
        stock_values_df = stock_values_df.rename(columns={stock_value_column_name: self.stock_value_column_name})
        return stock_values_df
