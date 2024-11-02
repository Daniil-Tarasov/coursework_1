from src.utils import get_data_from_excel, sort_date_operations, greeting_user, operations_cards, top_five_transactions, \
    currency_rates, stock_prices


def web_main(date):
    operations = get_data_from_excel('../data/operations.xlsx')
    operations = sort_date_operations(operations, date)
    result = {
        'greeting': greeting_user(),
        'cards': operations_cards(operations),
        'top_transactions': top_five_transactions(operations),
        'currency_rates' : currency_rates(),
        'stock_prices': stock_prices()
    }
    return result

print(web_main('2021-01-11 10:12:56'))