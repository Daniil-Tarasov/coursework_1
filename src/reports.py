import json
from datetime import datetime
from typing import Optional

import pandas as pd


def recording_data(file_name):
    """Декоратор, который записывает в файл результат, который возвращает функция, формирующая отчет"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'w') as f:
                json.dump(result, f)
            return result
        return wrapper
    return decorator


#@recording_data('spending_report.json')
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str]=None) -> pd.DataFrame:
    """Возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if date is None:
        date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    date = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    three_months_ago = date - pd.DateOffset(months=3)
    filtered_operations = transactions[transactions["Категория"] == category].copy()
    df_date = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y %H:%M:%S")
    filtered_operations = transactions[(three_months_ago <= df_date) & (df_date <= date)]
    result = filtered_operations['Сумма платежа'].sum()
    return pd.DataFrame(result)


df = pd.DataFrame({
    'Дата платежа': ['20.09.2021', '15.11.2021', '10.12.2021', '22.12.2021', '01.10.2021'],
    'Категория': ['Супермаркеты', 'Супермаркеты', 'Супермаркеты', 'Супермаркеты', 'Супермаркеты'],
    'Сумма платежа': [-200, -150, -546, 798, 400]
})
print(spending_by_category(df, 'Супермаркеты', '16.11.2021 00:00:00'))
