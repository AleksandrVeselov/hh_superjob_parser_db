from config import config
import psycopg2


def create_database(db_name):
    """Создание базы данных"""
    params = config()
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f'DROP DATABASE {db_name}')  # Пробуем удалить базу данных
    except psycopg2.errors.InvalidCatalogName:
        pass  # Перехватываем ошибку если базы данных с таким именем не существует

    cur.execute(f'CREATE DATABASE {db_name}')  # Создание базы данных
    params.update({'dbname': 'course_project_5'})

    cur.close()
    conn.close()


def create_table(table_name) -> None:
    """
    Создание таблицы с вакансиями из одной компании
    :param table_name: название компании, которое будет названием таблицы
    :param cur: курсор
    :return: None
    """
    conn = None
    params = config()
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(f'CREATE TABLE {table_name}'
                            f'(Name varchar(100),'
                            f'Min_salary int,'
                            f'Max_salary int,'
                            f'Currency int,'
                            f'URL varchar(100))')
                print("Таблица Skyeng успешно создана")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def add_data_to_database(data):
    """Заполнение базы данных"""