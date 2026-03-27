-- Write your PostgreSQL query statement below
WITH cte (departmentId, Salary) AS (
    SELECT DISTINCT departmentId,
    MAX(salary) OVER (PARTITION BY departmentId) AS Salary
    FROM Employee
)
SELECT d.name as Department, e.name as Employee, cte.Salary
FROM cte
INNER JOIN Employee e
ON cte.departmentId = e.departmentId AND cte.Salary = e.salary
INNER JOIN Department d
ON cte.departmentId = d.id