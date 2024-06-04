# Write your MySQL query statement below
select Department , Employee , Salary 
from (
select dept.name as Department , emp.name as Employee , Salary , dense_rank() over(partition by departmentId order by salary desc) as dr
from Employee emp inner join Department dept 
    on emp.departmentId = dept.id ) as newTable
where dr <= 3


