import utils
import classes
from config import config

DB_NAME = 'course_project_5'  # Название базы данных для проекта
TABLE_NAME = 'vacancies'  # Название таблицы для заполнения вакансиями
VACANCIES_COUNT = 300  # Ограничение максимального количества вакансий, чтобы не мучить Headhunter запросами


def main():
    """Функция для взаимодействия с пользователем"""

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

    hh_api = classes.HeadHunterAPI()  # Инициализация класса для работы с API сайта Headhunter

    # Приветствие пользователя, вывод списка компаний, заданных по умолчанию и предложение его изменить
    print('Привет, друг! Это курсовой проект по теме "Работа с базами данных.')
    input('Для продолжения нажми что-нибудь -> ')
    print('Сейчас произойдет получение открытых вакансий с сайта hh.ru для следующего перечня компаний:')
    print(*companies, sep='\n')

    while True:
        user_response = input('Хотите его изменить? - y/n -> ')

        # Изменение списка компаний
        if user_response.lower() == 'y':
            while True:

                flag = input('''Что сделать со списком:
                1 - Добавить в него компанию
                2 - Удалить из него компанию
                3 - Отмена
                ---> ''')

                if flag not in ('1', '2', '3'):
                    print('Введите корректный ответ')

                # Добавление в список компании
                if flag == '1':
                    company = input('Введите ключевое слово для поиска компании -> ')
                    founded_companies = hh_api.get_employer_id(company)  # Список найденных по запросу компаний

                    if founded_companies:
                        print('Вот что нашлось по Вашему запросу:')
                        print(*founded_companies, sep='\n')

                        id_for_adding = input('Для добавления в список введите id компании -> ')
                        utils.append_company(founded_companies, companies, id_for_adding)  # Добавление компании

                        print(f'Компания с ID {id_for_adding} успешно добавлена в список')
                        print('Обновленный список компаний: ')
                        print(*companies, sep='\n')

                    else:
                        print('К сожалению по вашему запросу ничего не найдено(')

                # Удаление из списка компании
                elif flag == '2':
                    id_for_deleting = input('Введите ID компании для ее удаления из списка -> ')
                    utils.delete_company(companies, id_for_deleting)

                    print(f'Компания с ID {id_for_deleting} успешно удалена из списка')
                    print('Обновленный список компаний: ')
                    print(*companies, sep='\n')

                # Выход из цикла и продолжение работы программы
                elif flag == '3':
                    break

            break

        # Выход из цикла и продолжение работы программы
        elif user_response.lower() == 'n':
            break

        else:
            print('Введите корректный ответ')

    params = config()  # Параметры для подключения к базе данных
    utils.create_database(DB_NAME, params)  # создание базы данных
    params.update({'dbname': DB_NAME})  # обновление параметров для подключения к базе данных
    print(f"БД {DB_NAME} успешно создана")

    utils.create_table(TABLE_NAME, params)  # Создание в базе данных таблицы для заполнения
    print(f"Таблица {TABLE_NAME} успешно создана")

    # заполнение таблицы данными о вакансиях компании
    for company in companies:
        vac = hh_api.get_vacancies(company['id'],
                                   VACANCIES_COUNT)  # получение открытых вакансий соответствующей компании
        utils.add_data_to_database(TABLE_NAME, vac, params)
        print(f"Таблица {TABLE_NAME} успешно заполнена вакансиями компании {company['name']}")

    db_manager = classes.DBManager(params)  # Создание экземпляра класса DBManager для работы с БД

    while True:
        user_response = input("""Возможности работы с базой данных:
        1 - Вывести список всех компаний и количество вакансий у каждой компании.
        2 - Вывести список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию
        3 - Вывести среднюю зарплату по всем вакансиям.
        4 - Вывести список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        5 - Вывести список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
        6 - Выход из программы.
        --> """)

        if user_response not in ('1', '2', '3', '4', '5', '6'):
            print('Введите корректный ответ')

        # Выход
        elif user_response == '6':
            break

        # Поиск по ключевому слову
        elif user_response == '5':
            keyword = input('Введите ключевое слово для поиска в названии вакансии -> ')
            rows = db_manager.manager(user_response, TABLE_NAME, keyword)  # результат работы SQL запроса
            if rows:
                print(*rows, sep='\n')
            else:
                print('По введенному ключевому слову вакансий не найдено(')

        # Всё остальное
        else:
            rows = db_manager.manager(user_response, TABLE_NAME)  # результат работы SQL запроса
            print(*rows, sep='\n')


if __name__ == '__main__':
    main()
