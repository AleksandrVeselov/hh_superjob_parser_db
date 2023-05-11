from config import config
import psycopg2


def create_database(db_name, params):
    """Создание базы данных"""
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f'DROP DATABASE {db_name}')  # Пробуем удалить базу данных
    except psycopg2.errors.InvalidCatalogName:
        pass  # Перехватываем ошибку если базы данных с таким именем не существует

    cur.execute(f'CREATE DATABASE {db_name}')  # Создание базы данных

    cur.close()
    conn.close()


def create_table(table_name, params) -> None:
    """
    Создание таблицы с вакансиями из одной компании
    :param table_name: название компании, которое будет названием таблицы
    :param: params: параметры для подключения к базе данных
    :return: None
    """
    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(f'CREATE TABLE "{table_name}"'
                            f'(Name varchar(100),'
                            f'Area varchar(50),'
                            f'Min_salary int,'
                            f'Max_salary int,'
                            f'Currency varchar(50),'
                            f'Employer varchar(50),'
                            f'URL varchar(100))')
                print("Таблица Skyeng успешно создана")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def add_data_to_database(table_name, data: list[dict], params) -> None:
    """
    Функция для заполнения таблицы базы данных
    :param data: список с вакансиями компании
    :param params: параметры для подключения к базе данных
    :return:
    """
    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                for vacancy in data:

                    # Если по ключу salary есть словарь
                    if vacancy['salary']:
                        salary_min, salary_max = vacancy['salary']['from'], vacancy['salary']['to']  # мин/макс зарплата
                        currency = vacancy['salary']['currency']  # валюта

                        if not salary_min:
                            salary_min = 0  # если не указана минимальная зарплата, приравниваем ее к нулю
                        if not salary_max:
                            salary_max = 0  # если не указана максимальная зарплата, приравниваем ее к нулю

                    # Если по ключу salary возвращается None
                    else:
                        salary_min = salary_max = 0
                        currency = 'RUR'

                    # Запрос на языке SQL для заполнения таблицы
                    cur.execute(f'INSERT INTO "{table_name}" '
                                f'VALUES (%s, %s, %s, %s, %s, %s, %s)', (vacancy['name'], vacancy['area']['name'],
                                                                         salary_min,
                                                                         salary_max,
                                                                         currency,
                                                                         vacancy['alternate_url'],
                                                                         vacancy['employer']['name']))

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
