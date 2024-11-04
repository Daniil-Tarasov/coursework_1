import json
from datetime import datetime
from typing import Callable, Optional

import pandas as pd


def recording_data(file_name) -> Callable:
    """Декоратор, который записывает в файл результат, который возвращает функция, формирующая отчет"""

    def decorator(func) -> Callable:
        def wrapper(*args, **kwargs) -> json:
            result = func(*args, **kwargs)
            with open(file_name, "w") as f:
                json.dump(result, f)
            return result

        return wrapper

    return decorator


# @recording_data('spending_report.json')
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if date is None:
        date = datetime.now()
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    three_months_ago = date - pd.DateOffset(months=3)
    filtered_operations = transactions[transactions["Категория"] == category].copy()
    df_date = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y")
    filtered_operations = transactions[(three_months_ago <= df_date) & (df_date <= date)]
    result = filtered_operations["Сумма операции с округлением"].sum()
    return pd.DataFrame({"Траты": [result]})
