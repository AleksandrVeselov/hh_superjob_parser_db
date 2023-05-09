import requests
class HeadHunterAPI:
    """Класс определяющий функционал для работы с api сайта HeadHunter"""
    URL = 'https://api.hh.ru/vacancies'

    def get_request(self, company, page, per_page=100):
        """
        Отправка запроса на API
        :param company: название компании
        :param page: номер страницы
        :param per_page: количество вакансий на одной странице
        :return: json со списком вакансий
        """

        # в параметрах задана сортировка по дате и только с указанной зарплатой в рублях по России
        params = {'text': keyword,
                  'page': page,
                  'per_page': per_page,
                  'order_by': "publication_time",
                  }

        response = requests.get(self.URL, params=params).json()
        return response['items']

    def get_vacancies(self, company: str) -> list[json]:
        """

        :param company: компания, для которой нужно получить список вакансий
        :return: список с вакансиями на соответствующей странице
        """
        # Максимальное количество вакансий для парсинга - 2000
        if pages > 20:
            raise ValueError('Вы превысили максимальное число вакансий, возможных для парсинга по API')

        vacancies = []  # список с вакансиями
        for page in range(pages):
            page = self.get_request(keyword, page, area)
            vacancies.extend(page)

        return vacancies