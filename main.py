from src.class_api import HeadHunterAPI
from utils.add_info_to_database import add_info_to_database
from src.class_dbmanager import DBManager


if __name__ == '__main__':
    HeadHunterAPI.get_vacancies()
    add_info_to_database()
    print('')
    while True:
        def_list = [DBManager.get_companies_and_vacancies_count, DBManager.get_all_vacancies,
                    DBManager.get_avg_salary, DBManager.get_vacancies_with_higher_salary,
                    DBManager.get_vacancies_with_keyword]

        print("1. Get a list of all companies and the number of vacancies for each company.")
        print("2. Get a list of all vacancies with the company name, vacancy name and salary,"
              " and a link to the vacancy.")
        print("3. Get an average salary for vacancies.")
        print("4. Get a list of all jobs that have a salary above the average for all jobs.")
        print("5. Get a list of all jobs that have 'keyword' in their title.")
        print("6. Exit.")
        print('')

        user_choice = input('Enter: ')

        if user_choice not in ('1', '2', '3', '4', '5', '6'):
            print("Wrong action.")
            continue

        elif user_choice == '6':
            break
        else:
            def_list[int(user_choice) - 1]()
            print('')




