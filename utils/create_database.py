import psycopg2


def create_database():
    connection = psycopg2.connect(host='localhost', database='postgres',  user='postgres', password='bubacock')
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute('DROP DATABASE IF EXISTS "head_hunter_jobs"')
    cursor.execute('CREATE DATABASE "head_hunter_jobs"'
                   ' WITH'
                   ' OWNER = postgres'
                   ' ENCODING = \'UTF8\''
                   ' CONNECTION LIMIT = -1'
                   ' IS_TEMPLATE = False;')

    connection.commit()
    connection.close()

