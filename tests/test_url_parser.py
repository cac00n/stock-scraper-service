import pandas as pd
import pytest
from pytest_mock import MockerFixture

from stock_scraper_service.config import UrlScraperSettings
from stock_scraper_service.url_info import BaseUrl, Currency, StockMarket
from stock_scraper_service.url_parser import StockScraper

MOCKED_DATA_DF = pd.DataFrame({"Schluss": [22.3, 12.1, 20.2], "Erster": [3.1, 2.1, 0.2], "Datum": [0, 1, 2]})


class TestStockScraper:
    @pytest.fixture
    def stock_scraper(self) -> StockScraper:
        settings = UrlScraperSettings(
            base_url=BaseUrl.ariva,
            currency=Currency.eur,
            stock_market=StockMarket.xetra,
            datetime_column_name="Datum",
            stock_value_column_name="Schluss",
            decimal_separator=",",
            thousands_separator=".",
        )
        return StockScraper(settings)

    def test_scrape_stock_information(self, stock_scraper: StockScraper, mocker: MockerFixture) -> None:
        read_html_mock = mocker.patch.object(pd, "read_html", return_value=[MOCKED_DATA_DF])
        actual_stock_values_df = stock_scraper.scrape_stock_information()
        expected_stock_values = pd.DataFrame(
            {stock_scraper.stock_value_column_name: MOCKED_DATA_DF["Schluss"]},
            index=pd.Index(MOCKED_DATA_DF["Datum"], name=stock_scraper.datetime_column_name),
        )

        pd.testing.assert_frame_equal(actual_stock_values_df, expected_stock_values)
        read_html_mock.assert_called_once_with(
            stock_scraper.generate_url(),
            match=stock_scraper.url_settings.stock_value_column_name,
            header=0,
            decimal=stock_scraper.url_settings.decimal_separator,
            thousands=stock_scraper.url_settings.thousands_separator,
            converters={stock_scraper.url_settings.datetime_column_name: stock_scraper._transform_to_datetime_format},
        )

    @pytest.mark.parametrize("url", BaseUrl)
    @pytest.mark.parametrize("currency", Currency)
    @pytest.mark.parametrize("stock_market", StockMarket)
    def test_generate_url(self, url: BaseUrl, currency: Currency, stock_market: StockMarket) -> None:
        settings = UrlScraperSettings(
            base_url=url,
            currency=currency,
            stock_market=stock_market,
            datetime_column_name="dummy",
            stock_value_column_name="dummy",
            decimal_separator="dummy",
            thousands_separator="dummy",
        )
        stock_scraper = StockScraper(settings)
        actual_result: str = stock_scraper.generate_url()
        expected_result: str = url.format(currency=currency, stock_market=stock_market)
        assert actual_result == expected_result

    def test_clean_currency_values(self, stock_scraper: StockScraper) -> None:
        cleaned_data_df = stock_scraper._clean_currency_values(MOCKED_DATA_DF)
        expected_stock_values = pd.DataFrame(
            {stock_scraper.stock_value_column_name: MOCKED_DATA_DF["Schluss"]},
            index=pd.Index(MOCKED_DATA_DF["Datum"], name=stock_scraper.datetime_column_name),
        )
        pd.testing.assert_frame_equal(cleaned_data_df, expected_stock_values)

    @pytest.mark.parametrize("datetime", [100819, "100819"])
    def test_transform_to_datetime_format(self, stock_scraper: StockScraper, datetime: str | int) -> None:
        actual_time_stamp: pd.Timestamp = stock_scraper._transform_to_datetime_format(datetime)
        expected_time_stampe = pd.Timestamp("2019-08-10 00:00:00")
        assert actual_time_stamp == expected_time_stampe
