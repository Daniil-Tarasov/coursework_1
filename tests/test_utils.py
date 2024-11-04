import pytest
from datetime import datetime
from typing import Any
from unittest.mock import patch, mock_open

import pandas as pd

from src.utils import (
    get_data_from_excel,
    sort_date_operations,
    greeting_user,
    top_five_transactions,
    operations_cards,
    stock_prices, currency_rates,
)


@patch("builtins.open", new_callable=mock_open, read_data=b"\x3c\x80\x00\x00\x00")
@patch("pandas.read_excel")
def test_get_data_from_excel(mock_read_excel: Any, mock_file: Any) -> None:
    mock_read_excel.return_value = pd.DataFrame({"amount": [100], "currency": ["USD"]})
    transactions = get_data_from_excel("data/transactions.xlsx")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_not_found_excel(mock_file: Any) -> None:
    transactions = get_data_from_excel("data/transactions.xlsx")
    assert transactions == []


def test_sort_date_operations(operations_list: list) -> None:
    assert sort_date_operations(operations_list, "2022-01-10 11:15:21") == [
        {
            "Дата операции": "10.01.2022 10:04:26",
            "Дата платежа": "11.01.2021",
            "Номер карты": "",
            "Статус": "OK",
            "Сумма операции": -9925.84,
            "Валюта операции": "RUB",
            "Сумма платежа": -9925.84,
            "Валюта платежа": "RUB",
            "Кэшбэк": "",
            "Категория": "ЖКХ",
            "MCC": "",
            "Описание": "ЖКУ Квартира",
            "Бонусы (включая кэшбэк)": 99,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 9925.84,
        }
    ]


@pytest.mark.parametrize(
    ("now_datetime", "expected_greeting"),
    [
        (datetime(2024, 1, 1, hour=6, minute=0), "Доброе утро"),
        (datetime(2024, 1, 1, hour=14, minute=0), "Добрый день"),
        (datetime(2024, 1, 1, hour=20, minute=0), "Добрый вечер"),
        (datetime(2024, 1, 1, hour=3, minute=0), "Доброй ночи"),
    ],
)
@patch("src.utils.datetime")
def test_get_greeting(mocked_datetime, now_datetime, expected_greeting):
    mocked_datetime.now.return_value = now_datetime
    assert greeting_user() == expected_greeting


def test_operations_cards() -> None:
    assert operations_cards([{"Номер карты": "*1234", "Сумма операции": -1.0}]) == [
        {"last_digits": "1234", "total_spent": 1.0, "cashback": 0.01}
    ]


def test_top_five_transactions(small_operations_list) -> None:
    assert top_five_transactions(small_operations_list) == [
        {"date": "11.01.2021", "amount": 9925.84, "category": "ЖКХ", "description": "ЖКУ Квартира"}
    ]


@patch("requests.get")
@patch("requests.get")
def test_currency_rates(mock_usd, mock_eur) -> None:
    mock_usd.return_value.status_code = 200
    mock_eur.return_value.status_code = 200
    mock_usd.return_value.json.return_value = {'data': {'RUB': {'value': 1.00}}}
    mock_eur.return_value.json.return_value = {'data': {'RUB': {'value': 1.00}}}
    assert currency_rates() == [
        {
            'currency': 'USD',
            'rate': 1.00
        },
        {
            'currency': 'EUR',
            'rate': 1.00
        }
    ]


@patch("requests.get")
def test_stock_prices(mock_convert):
    mock_convert.return_value.status_code = 200
    mock_convert.return_value.json.return_value = {"data": {"symbol": "AAPL", "close": 1.0}}
    assert stock_prices() == [{"stock": "AAPL", "price": 1.0}]
