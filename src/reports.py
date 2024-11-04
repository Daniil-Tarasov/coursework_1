import json
import logging
import os
from datetime import datetime
from typing import Callable, Optional

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/reports.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("reports")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
    logger.info("Ищем траты по конкретной категории")
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    three_months_ago = date - pd.DateOffset(months=3)
    filtered_operations = transactions[transactions["Категория"] == category].copy()
    df_date = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y")
    filtered_operations = transactions[(three_months_ago <= df_date) & (df_date <= date)]
    result = filtered_operations["Сумма операции с округлением"].sum()
    return pd.DataFrame({"Траты": [result]})
