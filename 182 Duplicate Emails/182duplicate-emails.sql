-- Write your PostgreSQL query statement below
SELECT DISTINCT t1.email as Email
FROM Person t1
INNER JOIN Person t2 
ON t1.id != t2.id AND t1.email = t2.email;