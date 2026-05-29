-- Write your PostgreSQL query statement below
SELECT ROUND(CAST(SUM(tiv_2016) AS NUMERIC), 2) AS tiv_2016
FROM Insurance i1
WHERE NOT EXISTS (
    SELECT 1
    FROM Insurance i2
    WHERE i1.lat = i2.lat AND i1.lon = i2.lon AND i1.pid != i2.pid
) AND EXISTS (
    SELECT 1
    FROM Insurance i3
    WHERE i1.tiv_2015 = i3.tiv_2015 AND i1.pid != i3.pid
);