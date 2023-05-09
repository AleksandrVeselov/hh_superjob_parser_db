import psycopg2
import requests
import utils
from classes import HeadHunterAPI


def main():
    """"""
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
    hh_api = HeadHunterAPI()
    # vac = hh_api.get_vacancies(1122462)  # список словарей с открытыми вакансиями компании по ключу vacancies_url
    utils.create_database('course_project_5')
    print(f"БД успешно создана")
    utils.create_table('Skyeng')
    print("Таблица успешно создана")




if __name__ == '__main__':
    main()
