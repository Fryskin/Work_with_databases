import json
import psycopg2
import os

from utils.create_database import create_database


def add_info_to_database():
    """Takes json file with vacancies and loads all info into database from this file."""

    create_database()

    connection = psycopg2.connect(host='localhost', database='head_hunter_jobs', user='postgres', password='bubacock')
    try:
        with connection.cursor() as cursor:

            file_path = os.path.join('utils', 'head_hunter_jobs.json')

            cursor.execute("CREATE TABLE vacancies "
                           " (title varchar(100) NOT NULL,"
                           " url text,salary_from int,"
                           " salary_to int,"
                           " company varchar(100));")

            with open(file_path) as json_file:
                content = json.load(json_file)

                for vacancy in content:
                    company_name = vacancy['employer']['name']
                    vacancy_title = vacancy['name']
                    vacancy_url = vacancy['alternate_url']

                    try:
                        salary_from = vacancy['salary']['from']

                    except TypeError:
                        salary_from = None

                    try:
                        salary_to = vacancy['salary']['to']

                    except TypeError:
                        salary_to = None

                    cursor.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)",
                                   (vacancy_title, vacancy_url, salary_from, salary_to, company_name))
                    connection.commit()

    finally:
        connection.close()
        os.remove(file_path)
        print('COMPLETE.')




