# Write your MySQL query statement below
-- SELECT COALESCE(
--     (SELECT Salary
--      FROM Employee e1
--      WHERE Salary < (SELECT MAX(Salary) FROM Employee e2 WHERE e1.Salary < e2.Salary)
--      ORDER BY Salary DESC
--      FETCH NEXT 1 ROW ONLY),
--     NULL
-- ) AS SecondHighestSalary;
select COALESCE(
    (select salary 
    from 
    (select salary, dense_rank() over (order by salary desc) as RN
    from employee ) as newtable
    where rn = 2
    limit 1 )
, NULL) as secondHighestSalary 
