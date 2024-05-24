# Write your MySQL query statement below
select product_name , sum(unit) as unit
from products pro inner join orders  ord 
on pro.product_id = ord.product_id
where order_date between 20200201 and 20200229
group by pro.product_id 
having sum(unit) >= 100