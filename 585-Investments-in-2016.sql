# Write your MySQL query statement below
select round(sum(tiv_2016) , 2)as tiv_2016
from insurance 
where pid  in (
select pid from (
select pid , dense_rank() over(order by lat , lon ) as dr
from insurance ) as newTable
group by dr 
having count(dr) = 1) 
and pid not in (
    select pid from (    
    select pid , count(tiv_2015) as countt
    from insurance
    group by tiv_2015 ) test1 
    where countt = 1)