Заполняет данными таблицу.
INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)

Получает список всех компаний и количество вакансий у каждой компании.
SELECT company, COUNT(*) FROM vacancies
GROUP BY company
ORDER BY company;

Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
SELECT * FROM vacancies
ORDER BY company;

Получает среднюю зарплату по вакансиям.
SELECT ROUND(AVG(salary_from)) AS from FROM vacancies;

Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
SELECT * FROM vacancies
WHERE salary_from > (SELECT ROUND(AVG(salary_from)) AS from FROM vacancies);

Получает список всех вакансий, в названии которых содержится 'keyword'.
SELECT * FROM vacancies
WHERE title LIKE '%keyword%';