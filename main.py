import requests

from classes import HeadHunterAPI


def main():
    """"""
    companies = [{'name': 'Ключевые системы и компоненты', 'id': 3403877},
                 {'name': 'Skyeng', 'id': 1122462},
                 {'name': 'СБЕР', 'id': 3529},
                 {'name': 'ВТБ', 'id': 4181},
                 {'name': 'Иннотех, Группа компаний', 'id': 4649269},
                 {'name': 'Ростелеком', 'id': 2748},
                 {'name': 'РОСБАНК', 'id': 599},
                 {'name': 'ВсеИнструменты.ру', 'id': 208707},
                 {'name': 'билайн', 'id': 4934},
                 {'name': 'МТС', 'id': 3776}]  # Список компаний для парсинга
    hh_api = HeadHunterAPI()
    print(*hh_api.get_employer_id('ПАО МТС'), sep='\n')
    # vac = hh_api.get_vacancies(1122462)  # список словарей с открытыми вакансиями компании по ключу vacancies_url
    # print(*vac, sep='\n')





if __name__ == '__main__':
    main()
