# Парсер вакансий с сайтов hh.ru & superjob

## О проекте

- Получение данных о работодателях и их вакансиях с сайта http://hh.ru/. Для этого используется публичный API http://hh.ru/ и библиотека `requests`.
- По умолчанию выбрано 10 компаний, от которых получаются данные о вакансиях по API(Ключевые системы и компоненты, Тензор, SberTech, ИК СИБИНТЕК, Иннотех, ИнфоТеКС,   Первый Бит, IBS, Университет Иннополис, Softline). Есть возмажность список изменить (добавить в него компанию, или удалить). При выборе опции "Добавить" программа   предлагает ввести название компании, затем выдает список найденных компаний. Для добавления компании в список нужно ввести ее ID.
- Создание БД course_project_5 и таблицы vacancies для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотека `psycopg2`.
- Заполнение таблицы vacancies в БД course_project_5 данными о работодателях и их вакансиях.
- Работа с базой данных происходит через класс DBManager.
Основные возможности при работе с базой данных:
- получение списка всех компаний и количества вакансий у каждой компании.
- получение списка всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
- получение средней зарплаты по вакансиям.
- получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
- получение списка всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.

В коде проекта технически ограничено максимальное количество вакансий для каждой компании до 300, чтобы не мучить hh.ru запросами и программа работала быстрее.

