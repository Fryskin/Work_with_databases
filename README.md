This program creates the database with two tables: companies, vacancies. Then takes all info about vacancies from hh ru api.
After this, full up the tables with info from api. Also, There are 5 class methods for working with DB:

get_companies_and_vacancies_count(Gets a list of all companies and the number of vacancies for each company.),

get_all_vacancies(Gets a list of all vacancies with the company name, vacancy name and salary, and a link to the vacancy.),

get_avg_salary(Receives an average salary for vacancies.),

get_vacancies_with_higher_salary(Gets a list of all jobs that have a salary above the average for all jobs.),

get_vacancies_with_keyword(Gets a list of all jobs that have 'keyword' in their title.).