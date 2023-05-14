import psycopg2
import requests


class HeadHunterAPI:
    """Класс определяющий функционал для работы с api сайта HeadHunter"""
    URL = 'https://api.hh.ru/vacancies'  # URL для поиска вакансий

    def get_request(self, employer_id, page, per_page=100):
        """
        Отправка запроса на API
        :param employer_id: id компании работодателя
        :param page: номер страницы
        :param per_page: количество вакансий на одной странице
        :return: json со списком вакансий
        """

        # в параметрах задана сортировка по дате
        params = {'employer_id': employer_id,
                  'page': page,
                  'per_page': per_page,
                  'order_by': "publication_time",
                  }

        response = requests.get(self.URL, params=params).json()
        return response['items']

    def get_vacancies(self, employer_id: int, count) -> list[dict]:
        """
        :param employer_id: id компании работодателя, для которой нужно получить список вакансий
        :param count: максимальное количество вакансий(если открытых вакансий больше count, вернется count вакансий)
        :return: список с вакансиями на соответствующей странице
        """
        vacancies = []  # список с вакансиями
        for page in range(20):
            if len(vacancies) < count:
                page = self.get_request(employer_id, page)
                if not page:
                    # Если в запросе нет вакансий, завершаем цикл
                    break
                vacancies.extend(page)
            else:
                break

        return vacancies

    @staticmethod
    def get_employer_id(employer: str) -> list[dict]:
        """
        Метод для получения информации о компании
        :param employer: ключевое слово для поиска компании
        :return: список с компаниями, найденными по переданному в метод ключевому слову
        """
        url = 'https://api.hh.ru/employers'  # URL для поиска работодателей
        params = {'text': employer,
                  'only_with_vacancies': True
                  }

        response = requests.get(url, params=params).json()
        return response['items']


class DBManager:
    """Класс для подключения к базе данных Postgress и работе с вакансиями, содержащимися в ней"""

    @staticmethod
    def get_companies_and_vacancies_count(table_name, cur):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        cur.execute(f'SELECT employer, count(*) FROM {table_name} GROUP BY employer')
        result = cur.fetchall()

        return result

    @staticmethod
    def get_all_vacancies(table_name, cur):
        """получает список всех вакансий с указанием названия компании, названия вакансии
        и зарплаты и ссылки на вакансию"""
        cur.execute(f'SELECT * FROM {table_name}')
        result = cur.fetchall()

        return result

    @staticmethod
    def get_avg_salary(table_name, cur):
        """получает среднюю зарплату по вакансиям"""
        cur.execute(f'SELECT AVG(min_salary) as average_min, '
                    f'AVG(max_salary) as average_max  FROM {table_name}')
        result = cur.fetchall()
        return result

    @staticmethod
    def get_vacancies_with_higher_salary(table_name, cur):
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        cur.execute(f'SELECT * FROM {table_name} '
                    f'WHERE min_salary > (SELECT AVG(min_salary) FROM {table_name})')
        result = cur.fetchall()
        return result

    @staticmethod
    def get_vacancies_with_keyword(table_name, keyword, cur):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""
        cur.execute(f"SELECT * FROM {table_name} "
                    f"WHERE name LIKE '%{keyword}%'")
        result = cur.fetchall()
        return result
