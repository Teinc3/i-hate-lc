-- Write your PostgreSQL query statement below
SELECT p.product_id, p.product_name
FROM Product p
WHERE NOT EXISTS (
    SELECT 1
    FROM Sales s
    WHERE p.product_id = s.product_id AND (
        s.sale_date < '2019-01-01' OR s.sale_date > '2019-03-31'
    )
) AND EXISTS (
    SELECT 1
    FROM Sales s2
    WHERE p.product_id = s2.product_id
);
