-- Write your PostgreSQL query statement below
WITH cte AS (
    SELECT id,
    departmentId,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM Employee
)
SELECT d.name AS Department, e.name AS Employee, e.salary as Salary
FROM cte
INNER JOIN Department d
ON cte.departmentId = d.id
INNER JOIN Employee e
ON cte.id = e.id
WHERE cte.rank <= 3;
