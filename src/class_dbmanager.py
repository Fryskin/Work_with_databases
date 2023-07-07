import psycopg2


class DBManager:
    """Class for working with DB Postgres."""

    @staticmethod
    def get_companies_and_vacancies_count():
        """Gets a list of all companies and the number of vacancies for each company."""

        connection = psycopg2.connect(host='localhost', database='head_hunter_jobs', user='postgres',
                                      password='bubacock')
        try:
            with connection.cursor() as cursor:

                cursor.execute("SELECT company, COUNT(*) FROM vacancies"
                               " GROUP BY company ORDER BY company;")
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Company: {row[0]}\nVacancies: {row[1]}')
                    print('-------------------------------------------')

                connection.commit()

        finally:
            connection.close()

    @staticmethod
    def get_all_vacancies():
        """Gets a list of all vacancies with the company name, vacancy name and salary, and a link to the vacancy."""

        connection = psycopg2.connect(host='localhost', database='head_hunter_jobs', user='postgres',
                                      password='bubacock')
        try:
            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM vacancies ORDER BY company;")
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Company: {row[4]}\nTitle: {row[0]}\nSalary from: {row[2]}\nSalary to: {row[3]}'
                          f'\nURL: {row[1]}')
                    print('-------------------------------------------')

                connection.commit()

        finally:
            connection.close()

    @staticmethod
    def get_avg_salary():
        """Receives an average salary for vacancies."""

        connection = psycopg2.connect(host='localhost', database='head_hunter_jobs', user='postgres',
                                      password='bubacock')

        try:
            with connection.cursor() as cursor:

                cursor.execute("SELECT ROUND(AVG(salary_from)) AS from FROM vacancies;")
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Average salary from: {row[0]} руб.')
                    print('-------------------------------------------')

                connection.commit()

        finally:
            connection.close()

    @staticmethod
    def get_vacancies_with_higher_salary():
        """Gets a list of all jobs that have a salary above the average for all jobs."""

        connection = psycopg2.connect(host='localhost', database='head_hunter_jobs', user='postgres',
                                      password='bubacock')

        try:
            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM vacancies"
                               " WHERE salary_from > (SELECT ROUND(AVG(salary_from)) AS from FROM vacancies);")
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Company: {row[4]}\nTitle: {row[0]}\nSalary from: {row[2]}\nSalary to: {row[3]}'
                          f'\nURL: {row[1]}')
                    print('-------------------------------------------')

                connection.commit()

        finally:
            connection.close()

    @staticmethod
    def get_vacancies_with_keyword():
        """Gets a list of all jobs that have 'keyword' in their title."""
        keyword = input('Enter the keyword: ')

        connection = psycopg2.connect(host='localhost', database='head_hunter_jobs', user='postgres',
                                      password='bubacock')

        try:
            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM vacancies"
                               f" WHERE title LIKE '%{keyword}%';")
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Company: {row[4]}\nTitle: {row[0]}\nSalary from: {row[2]}\nSalary to: {row[3]}'
                          f'\nURL: {row[1]}')
                    print('-------------------------------------------')

                connection.commit()

        finally:
            connection.close()

