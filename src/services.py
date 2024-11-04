import json
import re


def transactions_by_phone_numbers(operations: list) -> json:
    """Возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера"""
    phone_pattern = re.compile(
        r"\b(?:\+7|8)?\s*(909|919|929|949|959|970|980|997|999|\d{3})\s*\d{3}\s*[-]?\s*\d{2}\s*[-]?\s*\d{2}\b"
    )
    filtered_transactions = [
        operation
        for operation in operations
        if "Описание" in operation and phone_pattern.search(operation["Описание"])
    ]
    return json.dumps(filtered_transactions, ensure_ascii=False)
