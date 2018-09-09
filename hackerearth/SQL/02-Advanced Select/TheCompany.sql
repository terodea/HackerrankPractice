SELECT c.company_code,c.founder,
(SELECT count(distinct lead_manager_code) FROM Lead_Manager l WHERE l.company_code = c.company_code),
(SELECT count(distinct senior_manager_code) FROM Senior_Manager s WHERE s.company_code = c.company_code),
(SELECT count(distinct manager_code) FROM Manager m WHERE m.company_code = c.company_code),
(SELECT count(distinct employee_code) FROM Employee e WHERE e.company_code = c.company_code)
FROM Company c order by c.company_code ASC;
