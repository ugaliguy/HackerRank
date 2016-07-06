/*
Enter your query here.
*/
SELECT employee.company_code,company.founder,
COUNT(DISTINCT employee.lead_manager_code), COUNT(DISTINCT employee.senior_manager_code), 
COUNT(DISTINCT employee.manager_code), COUNT(DISTINCT employee.employee_code) 
FROM employee employee INNER JOIN company company 
ON employee.company_code = company.company_code 
GROUP BY employee.company_code,company.founder 
ORDER BY employee.company_code;