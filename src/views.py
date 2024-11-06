import json

import pandas as pd

from src.utils import (currency_rates, greeting_user, operations_cards, filter_date_operations,
                       stock_prices, top_five_transactions, convert_timestamps_to_strings)


def web_main(date: str) -> json:
    """Возвращает JSON для главной Веб-страницы"""
    operations = pd.read_excel("../data/operations.xlsx")
    operations = filter_date_operations(operations, date)
    operations = convert_timestamps_to_strings(operations)
    result = {
        "greeting": greeting_user(),
        "cards": operations_cards(operations),
        "top_transactions": top_five_transactions(operations),
        "currency_rates": currency_rates(),
        "stock_prices": stock_prices(),
    }
    return json.dumps(result, ensure_ascii=False)
