-- Write your PostgreSQL query statement below
SELECT DISTINCT t1.id, (
    CASE WHEN t2.id IS NOT NULL AND t3.p_id IS NOT NULL THEN 'Inner'
    WHEN t2.id IS NULL AND t3.p_id IS NOT NULL THEN 'Root'
    WHEN t2.id IS NOT NULL AND t3.p_id IS NULL THEN 'Leaf'
    ELSE 'Root'
    END
) AS type
FROM Tree t1
LEFT JOIN Tree t2
ON t1.p_id = t2.id
LEFT JOIN Tree t3 
ON t1.id = t3.p_id;