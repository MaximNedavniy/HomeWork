SELECT first_name, last_name FROM employees;
SELECT department_id FROM employees;
SELECT * FROM employees ORDER BY first_name;
SELECT first_name, last_name, salary, salary/100*12 AS PF FROM employees;
SELECT min(salary) AS min_salary, max(salary) AS max_salary FROM employees;
SELECT first_name, last_name,  ROUND(salary / 12, 2) AS monthly_salary FROM employees;

