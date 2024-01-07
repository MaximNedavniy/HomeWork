SELECT Employees.first_name, Employees.last_name, Employees.department_id, Department.department_name FROM Employees LEFT JOIN Department ON Employees.department_id = Department.department_id;

SELECT Employees.first_name, Employees.last_name, Department.department_name, Locations.city, Locations.state_province FROM Employees LEFT JOIN Department ON Employees.department_id = Department.department_id LEFT JOIN locations ON department.location_id = locations.location_id;

SELECT Employees.first_name, Employees.last_name, Employees.department_id, Department.department_name FROM Employees JOIN Department ON Employees.department_id = Department.department_id WHERE Employees.department_id IN (40, 80);

SELECT Department.department_name FROM Department;

SELECT e1.first_name AS first_name_employees, e2.first_name AS first_name_manager FROM employees e1 LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;

SELECT jobs.job_title, employees.last_name || ' ' || employees.first_name AS Full_employee_name, MAX(employees.salary) OVER (PARTITION BY jobs.job_id) - employees.salary AS salary_difference FROM employees JOIN jobs ON employees.job_id = jobs.job_id;

SELECT jobs.job_title, AVG(employees.salary) as Avg_Salary FROM employees JOIN jobs ON jobs.job_id=employees.job_id GROUP BY job_title;

SELECT employees.last_name || ' ' || employees.first_name AS Full_employee_name, employees.salary, locations.city FROM employees LEFT JOIN departments ON employees.department_id=departments.department_id LEFT JOIN locations ON departments.location_id=locations.location_id WHERE locations.city = "London";

SELECT jobs.job_title, count( jobs.job_title) as count_employees FROM employees JOIN jobs ON jobs.job_id=employees.job_id GROUP BY job_title;
