-- Write your PostgreSQL query statement below
UPDATE Salary s1
SET sex = (CASE
    WHEN s2.sex = 'm' THEN 'f'
    WHEN s2.sex = 'f' THEN 'm'
    ELSE null END
)
FROM Salary s2
WHERE s1.id = s2.id;