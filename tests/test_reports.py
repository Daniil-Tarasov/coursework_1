import pandas as pd
import pytest

from src.reports import spending_by_category


@pytest.fixture()
def transactions() -> pd.DataFrame:
    transactions_data = [
        {"Дата платежа": "20.09.2021", "Категория": "Супермаркеты", "Сумма операции с округлением": 200.00},
        {"Дата платежа": "15.11.2021", "Категория": "Супермаркеты", "Сумма операции с округлением": 150.00},
        {"Дата платежа": "10.12.2021", "Категория": "Супермаркеты", "Сумма операции с округлением": 100.00},
        {"Дата платежа": "22.12.2021", "Категория": "Другие", "Сумма операции с округлением": 50.00},
        {"Дата платежа": "01.10.2021", "Категория": "Супермаркеты", "Сумма операции с округлением": 100.00},
    ]
    transactions_df = pd.DataFrame(transactions_data)
    return transactions_df


def test_spending_by_category(transactions: pd.DataFrame) -> None:
    result_df = spending_by_category(transactions, "Супермаркеты", "2021-11-15 12:00:00")
    assert len(result_df) == 1


def test_spending_by_category_no_data(transactions: pd.DataFrame) -> None:
    result_df = spending_by_category(transactions, "Супермаркеты")
    assert len(result_df) == 1
    assert result_df["Траты"].values == 0
