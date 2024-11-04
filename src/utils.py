import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

import pandas as pd

load_dotenv()
for_currency = os.getenv('API_KEY_FOR_CURRENCY')
for_stoks = os.getenv('API_KEY_FOR_STOCK')


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
    card_operations = {}
    result = []
    for operation in operations:
        card_number = str(operation.get('Номер карты'))
        str_amount = str(operation.get('Сумма операции'))
        amount = str_amount[1:]
        if card_number != 'nan':
            last_digits = card_number[-4:]
            if last_digits in card_operations:
                card_operations[last_digits]['total_spent'] += float(amount)
            else:
                card_operations[last_digits] = {'total_spent': float(amount), 'cashback': 0}
            card_operations[last_digits]['cashback'] = card_operations[last_digits]['total_spent'] * 0.01
    for digits, data in card_operations.items():
        result.append({'last_digits': digits, 'total_spent': round(data['total_spent'], 2), 'cashback': data['cashback']})
    return result


def top_five_transactions(operations: list):
    """Возвращает топ-5 транзакций по сумме платежа"""
    sort_transaction = []
    sorted_operations = sorted(operations, key=lambda x: x['Сумма платежа'])
    top_transactions = sorted_operations[:5]
    for sort in top_transactions:
        date = sort['Дата операции'][:10]
        str_amount = str(sort.get('Сумма операции'))
        amount = str_amount[1:]
        sort_transaction.append({"date": date, 'amount': float(amount), 'category': sort['Категория'], 'description': sort['Описание']})
    return sort_transaction


def currency_rates():
    """Возвращает курсы валют"""
    result_usd = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={for_currency}&base_currency=USD&currencies=RUB")
    result_eur = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={for_currency}&base_currency=EUR&currencies=RUB")
    value_usd = result_usd.json()['data']['RUB']['value']
    value_eur = result_eur.json()['data']['RUB']['value']
    result = [
        {
            'currency': 'USD',
            'rate': round(value_usd, 2)
        },
        {
            'currency': 'EUR',
            'rate': round(value_eur, 2)
        }
    ]
    return result


def stock_prices():
    """Возвращает стоимость акций из S&P 500"""
    url = f"https://api.marketstack.com/v1/eod/latest?access_key={for_stoks}"
    result = []
    with open('../user_settings.json', encoding="utf-8") as file:
        user_stoks = json.load(file)
        user_stok = ','.join(user_stoks['user_stocks'])
        querystring = {"symbols": user_stok}
        response = requests.get(url, params=querystring)
        for data in response.json()['data']:
            result.append({'stock': data['symbol'], 'price': data['close']})
        return result
