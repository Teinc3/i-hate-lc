-- Write your PostgreSQL query statement below
WITH cte AS (
    SELECT managerId
    FROM Employee e1
    GROUP BY e1.managerId
    HAVING COUNT(managerId) >= 5
)
SELECT e2.name
FROM cte
INNER JOIN Employee e2
ON e2.id = cte.managerId
