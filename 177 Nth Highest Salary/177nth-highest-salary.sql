CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  IF N < 1
    THEN RETURN QUERY SELECT NULL::INT;
    RETURN;
  END IF;

  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT (
        SELECT DISTINCT e.salary
        FROM Employee e
        ORDER BY e.salary DESC
        OFFSET N-1
        LIMIT 1
    )
  );
END;
$$ LANGUAGE plpgsql;