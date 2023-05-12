import utils
import classes
from config import config

DB_NAME = 'course_project_5'  # Название базы данных для проекта
TABLE_NAME = 'vacancies'  # Название таблицы для заполнения вакансиями
VACANCIES_COUNT = 300  # Ограничение максимального количества вакансий для каждой компании


def main():
    """Главный скрипт проекта"""

    companies = [{'name': 'Ключевые системы и компоненты', 'id': 3403877},
                 {'name': 'Тензор', 'id': 67611},
                 {'name': 'SberTech', 'id': 906557},
                 {'name': 'ИК СИБИНТЕК', 'id': 197135},
                 {'name': 'Иннотех, Группа компаний', 'id': 4649269},
                 {'name': 'ИнфоТеКС', 'id': 3778},
                 {'name': 'Первый Бит', 'id': 3177},
                 {'name': 'IBS', 'id': 139},
                 {'name': 'Университет Иннополис', 'id': 1160188},
                 {'name': 'Softline', 'id': 2381}]  # Список компаний для парсинга

    params = config()  # Параметры для подключения к базе данных
    hh_api = classes.HeadHunterAPI()  # Инициализация класса для работы с сайтом Headhunter
    # print(hh_api.get_employer_id('СИБИНТЕК'))
    # utils.create_database(DB_NAME, params)  # создание базы данных
    params.update({'dbname': DB_NAME})  # обновление параметров для подключения к базе данных
    # print(f"БД успешно создана")
    # utils.create_table(TABLE_NAME, params)  # Создание таблицы для заполнения в базе данных
    # print("Таблица успешно создана")
    #
    # # заполнение таблицы данными о вакансиях компании
    # for company in companies:
    #     vac = hh_api.get_vacancies(company['id'], VACANCIES_COUNT)  # получение открытых вакансий соответствующей компании
    #     utils.add_data_to_database(TABLE_NAME, vac, params)
    #     print(f"Таблица успешно заполнена вакансиями компании {company['name']}")

    db_manager = classes.DBManager(params)
    rows = db_manager.get_vacancies_with_higher_salary(TABLE_NAME)
    print(*rows, sep='\n')


if __name__ == '__main__':
    main()
