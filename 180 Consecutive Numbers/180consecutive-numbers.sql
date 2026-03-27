-- Write your PostgreSQL quexry statement below
WITH cte AS (
    SELECT num,
    LEAD(num, 1) OVER (ORDER BY id) AS next_num_1,
    LEAD(num, 2) OVER (ORDER BY id) AS next_num_2
    FROM Logs
)
SELECT DISTINCT num as ConsecutiveNums
FROM cte
WHERE num = next_num_1 AND num = next_num_2;