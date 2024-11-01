import os
from datetime import datetime

import requests
from dotenv import load_dotenv

import pandas as pd

load_dotenv()
for_currency = os.getenv('API_KEY_FOR_CURRENCY')


def get_data_from_excel(path_to_the_file: str) -> list:
    """Функция, которая возвращает данные о финансовых транзакциях из файла excel"""
    try:
        pd.read_excel(path_to_the_file)

    except ValueError:

        return []

    except FileNotFoundError:

        return []

    else:
        operations = pd.read_excel(path_to_the_file)
        return operations.to_dict(orient="records")


def sort_date_operations(operations: list, date: str) -> list:
    """Сортирует операции за текущий месяц"""
    sorted_operations = []
    first_day_moth = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").replace(day=1)
    data_datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    for operation in operations:
        date_operation = datetime.strptime(operation["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if first_day_moth <= date_operation <= data_datetime:
            sorted_operations.append(operation)
    return sorted_operations


def greeting_user() -> str:
    """Возвращает приветствие в зависимости от времени суток"""
    current_hour = datetime.now().hour
    if current_hour < 6:
        return "Доброй ночи"
    elif current_hour < 12:
        return "Доброе утро"
    elif current_hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"


def operations_cards(operations: list):
    """Возвращает данные по каждой карте"""
    pass


def top_five_transactions(operations: list):
    """Возвращает топ-5 транзакций по сумме платежа"""
    sorted_operations = sorted(operations, key=lambda x: x['Сумма платежа'])
    top_transactions = sorted_operations[:5]
    return top_transactions


def currency_rates():
    """Возвращает курсы валют"""
    result_usd = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={for_currency}&base_currency=USD&currencies=RUB")
    result_eur = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={for_currency}&base_currency=EUR&currencies=RUB")
    value_usd = result_usd.json()['data']['RUB']['value']
    value_eur = result_eur.json()['data']['RUB']['value']
    return {'USD': value_usd,
            'EUR': value_eur
            }


def stock_prices():
    """Возвращает стоимость акций из S&P 500"""
    pass
