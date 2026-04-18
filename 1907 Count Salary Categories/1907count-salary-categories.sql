-- Write your PostgreSQL query statement below

WITH cte (category) AS (
    VALUES ('Low Salary'), ('Average Salary'), ('High Salary')
)

SELECT category, (COUNT(category) - 1) AS accounts_count
FROM (
    SELECT (
        CASE WHEN income < 20000 THEN 'Low Salary'
        WHEN income > 50000 THEN 'High Salary'
        ELSE 'Average Salary' END
    ) AS category
    FROM accounts
    UNION ALL
    SELECT category
    FROM cte
)
GROUP BY category