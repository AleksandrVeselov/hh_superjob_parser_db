import psycopg2
import requests
import utils
from classes import HeadHunterAPI
from config import config


def main():
    """Главный скрипт"""

    companies = [{'Ключевые системы и компоненты': 3403877},
                 {'Skyeng': 1122462},
                 {'СБЕР': 3529},
                 {'ВТБ': 4181},
                 {'Иннотех, Группа компаний': 4649269},
                 {'Ростелеком': 2748},
                 {'РОСБАНК': 599},
                 {'ВсеИнструменты.ру': 208707},
                 {'билайн': 4934},
                 {'МТС': 3776}]  # Список компаний для парсинга
    params = config()  # Параметры для подключения к базе данных
    hh_api = HeadHunterAPI()
    vac = hh_api.get_vacancies(3403877)  # список словарей с открытыми вакансиями компании по ключу vacancies_url
    print(*vac, sep='\n')
    utils.create_database('course_project_5', params)
    params.update({'dbname': 'course_project_5'})
    print(f"БД успешно создана")
    utils.create_table('Ключевые системы и компоненты', params)
    print("Таблица успешно создана")
    utils.add_data_to_database('Ключевые системы и компоненты', vac, params)
    # emp = hh_api.get_employers(25)
    # print(*emp, sep='\n')

if __name__ == '__main__':
    main()
