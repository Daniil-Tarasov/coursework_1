from src.services import transactions_by_phone_numbers


def test_transactions_by_phone_numbers(num_operations_list) -> None:
    assert transactions_by_phone_numbers(num_operations_list) == num_operations_list
