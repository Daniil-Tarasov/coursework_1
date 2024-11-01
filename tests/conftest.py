import pytest

@pytest.fixture
def operations_list() -> list:
    return  [
    {
        "Дата операции": "12.01.2021 10:30:58",
        "Дата платежа": "12.01.2021",
        "Номер карты": '',
        "Статус": "OK",
        "Сумма операции": 8000.0,
        "Валюта операции": "RUB",
        "Сумма платежа": 8000.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": 'nan',
        "Категория": "Пополнения",
        "MCC": 6012.0,
        "Описание": "Перевод с карты",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 8000.0,
    },
    {
        "Дата операции": "11.01.2021 23:10:44",
        "Дата платежа": "12.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -1423.6,
        "Валюта операции": "RUB",
        "Сумма платежа": -1423.6,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Ж/д билеты",
        "MCC": 4112.0,
        "Описание": "РЖД",
        "Бонусы (включая кэшбэк)": 28,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 1423.6,
    },
    {
        "Дата операции": "10.01.2022 10:04:26",
        "Дата платежа": "11.01.2021",
        "Номер карты": '',
        "Статус": "OK",
        "Сумма операции": -9925.84,
        "Валюта операции": "RUB",
        "Сумма платежа": -9925.84,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "ЖКХ",
        "MCC": '',
        "Описание": "ЖКУ Квартира",
        "Бонусы (включая кэшбэк)": 99,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 9925.84,
    },
    {
        "Дата операции": "11.01.2021 15:18:22",
        "Дата платежа": "11.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -798.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -798.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Магнит",
        "Бонусы (включая кэшбэк)": 15,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 798.0,
    },
    {
        "Дата операции": "11.01.2021 15:03:59",
        "Дата платежа": "11.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -285.85,
        "Валюта операции": "RUB",
        "Сумма платежа": -285.85,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Магнит",
        "Бонусы (включая кэшбэк)": 5,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 285.85,
    },
    {
        "Дата операции": "11.01.2021 14:26:09",
        "Дата платежа": "11.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -383.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -383.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "IP Gorskaya Vv",
        "Бонусы (включая кэшбэк)": 7,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 383.0,
    },
    {
        "Дата операции": "10.01.2021 16:47:17",
        "Дата платежа": "10.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -151.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -151.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5499.0,
        "Описание": "DIVAGE",
        "Бонусы (включая кэшбэк)": 3,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 151.0,
    },
    {
        "Дата операции": "10.01.2021 11:38:57",
        "Дата платежа": "10.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -68.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -68.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": 'nan',
        "Категория": "Супермаркеты",
        "MCC": 5499.0,
        "Описание": "DIVAGE",
        "Бонусы (включая кэшбэк)": 1,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 68.0,
    },
    {
        "Дата операции": "10.01.2021 01:44:42",
        "Дата платежа": "10.01.2021",
        "Номер карты": "*4556",
        "Статус": "OK",
        "Сумма операции": -250.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -250.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Связь",
        "MCC": 4814.0,
        "Описание": "МТС",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 250.0,
    },
    {
        "Дата операции": "09.01.2021 19:26:58",
        "Дата платежа": "09.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -160.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -160.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Сервис",
        "MCC": 7311.0,
        "Описание": "Auto",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 160.0,
    },
    {
        "Дата операции": "09.01.2021 18:50:56",
        "Дата платежа": "09.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -145.96,
        "Валюта операции": "RUB",
        "Сумма платежа": -145.96,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5499.0,
        "Описание": "DIVAGE",
        "Бонусы (включая кэшбэк)": 2,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 145.96,
    },
    {
        "Дата операции": "09.01.2021 10:36:19",
        "Дата платежа": "09.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -118.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -118.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Сервис",
        "MCC": 7311.0,
        "Описание": "Auto",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 118.0,
    },
    {
        "Дата операции": "08.01.2021 13:55:46",
        "Дата платежа": "08.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -28.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -28.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5499.0,
        "Описание": "Magazin 14",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 28.0,
    },
    {
        "Дата операции": "07.01.2021 16:49:20",
        "Дата платежа": "07.01.2021",
        "Номер карты": '',
        "Статус": "OK",
        "Сумма операции": -800.0,
        "Валюта операции": "RUB",
        "Сумма платежа": -800.0,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Переводы",
        "MCC": '',
        "Описание": "Константин Л.",
        "Бонусы (включая кэшбэк)": 0,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 800.0,
    },
    {
        "Дата операции": "02.01.2021 17:38:16",
        "Дата платежа": "02.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -1059.88,
        "Валюта операции": "RUB",
        "Сумма платежа": -1059.88,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Магнит",
        "Бонусы (включая кэшбэк)": 21,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 1059.88,
    },
    {
        "Дата операции": "01.01.2021 18:08:23",
        "Дата платежа": "01.01.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -815.68,
        "Валюта операции": "RUB",
        "Сумма платежа": -815.68,
        "Валюта платежа": "RUB",
        "Кэшбэк": '',
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Дикси",
        "Бонусы (включая кэшбэк)": 16,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 815.68,
    },
]


@pytest.fixture
def small_operations_list() -> list:
    return [{'Дата операции': '11.01.2021 16:04:26', 'Дата платежа': '11.01.2021', 'Номер карты': '', 'Статус': 'OK', 'Сумма операции': -9925.84, 'Валюта операции': 'RUB', 'Сумма платежа': -9925.84, 'Валюта платежа': 'RUB', 'Кэшбэк': 'nan', 'Категория': 'ЖКХ', 'MCC': 'nan', 'Описание': 'ЖКУ Квартира', 'Бонусы (включая кэшбэк)': 99, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 9925.84}, {'Дата операции': '11.01.2021 23:10:44', 'Дата платежа': '12.01.2021', 'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -1423.6, 'Валюта операции': 'RUB', 'Сумма платежа': -1423.6, 'Валюта платежа': 'RUB', 'Кэшбэк': '', 'Категория': 'Ж/д билеты', 'MCC': 4112.0, 'Описание': 'РЖД', 'Бонусы (включая кэшбэк)': 28, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 1423.6}, {'Дата операции': '11.01.2021 15:18:22', 'Дата платежа': '11.01.2021', 'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -798.0, 'Валюта операции': 'RUB', 'Сумма платежа': -798.0, 'Валюта платежа': 'RUB', 'Кэшбэк': '', 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Магнит', 'Бонусы (включая кэшбэк)': 15, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 798.0}, {'Дата операции': '11.01.2021 14:26:09', 'Дата платежа': '11.01.2021', 'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -383.0, 'Валюта операции': 'RUB', 'Сумма платежа': -383.0, 'Валюта платежа': 'RUB', 'Кэшбэк': 'nan', 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'IP Gorskaya Vv', 'Бонусы (включая кэшбэк)': 7, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 383.0}, {'Дата операции': '11.01.2021 15:03:59', 'Дата платежа': '11.01.2021', 'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -285.85, 'Валюта операции': 'RUB', 'Сумма платежа': -285.85, 'Валюта платежа': 'RUB', 'Кэшбэк': 'nan', 'Категория': 'Супермаркеты', 'MCC': 5411.0, 'Описание': 'Магнит', 'Бонусы (включая кэшбэк)': 5, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 285.85}]