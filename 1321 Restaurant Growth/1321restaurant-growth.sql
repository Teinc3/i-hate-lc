-- Write your PostgreSQL query statement below
WITH cte AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT visited_on, SUM(amount) AS amount, ROUND(AVG(amount), 2) AS average_amount
FROM (
    SELECT c1.visited_on, c2.amount
    FROM cte c1
    INNER JOIN cte c2
    ON c1.visited_on - c2.visited_on BETWEEN 0 AND 6
)
GROUP BY visited_on
HAVING COUNT(*) = 7
ORDER BY visited_on ASC;