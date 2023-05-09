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

    def get_vacancies(self, employer_id: int) -> list[dict]:
        """
        :param employer_id: id компании работодателя, для которой нужно получить список вакансий
        :return: список с вакансиями на соответствующей странице
        """
        vacancies = []  # список с вакансиями
        for page in range(20):
            page = self.get_request(employer_id, page)
            if not page:
                # Если в запросе нет вакансий, завершаем цикл
                break
            vacancies.extend(page)

        return vacancies

    @staticmethod
    def get_employer_id(employer: str) -> list[dict]:
        """
        Получение информации о компании для дальнейшего использования в методах класса
        :param employer:
        :return:
        """
        url = 'https://api.hh.ru/employers'  # URL для поиска работодателей
        params = {'text': employer,
                  'per_page': 100,
                  }

        response = requests.get(url, params=params).json()
        return response['items']


class DBManager:
    """Класс для подключения к базе данных Postgress и работе с вакансиями, содержащимися в ней"""

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии
        и зарплаты и ссылки на вакансию"""

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""

    def get_vacancies_with_higher_salary(self):
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”"""

