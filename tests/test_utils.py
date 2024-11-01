import os
from typing import Any
from unittest.mock import patch, mock_open

import pandas as pd
from dotenv import load_dotenv

from src.utils import get_data_from_excel, sort_date_operations, greeting_user, top_five_transactions


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
    assert sort_date_operations(operations_list, '2022-01-10 11:15:21') == [{
        "Дата операции": "10.01.2022 10:04:26",
        "Дата платежа": "11.01.2021",
        "Номер карты": '',
        "Статус": "OK",
        "Сумма операции": -9925.84,
        "Валюта операции": "RUB",
        "Сумма платежа": -9925.84,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "ЖКХ",
        "MCC": '',
        "Описание": "ЖКУ Квартира",
        "Бонусы (включая кэшбэк)": 99,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 9925.84,
    }]


def test_greeting_user() -> None:
    assert greeting_user() == "Добрый вечер"


def test_operations_cards() -> None:
    pass


def test_top_five_transactions(small_operations_list) -> None:
    assert top_five_transactions(small_operations_list) == small_operations_list


@patch('requests.get')
@patch('requests.get')
def test_currency_rates(mock_usd, mock_eur) -> None:
    load_dotenv()
    for_currency = os.getenv('API_KEY_FOR_CURRENCY')
    headers ={'apikey': for_currency}
    pass
