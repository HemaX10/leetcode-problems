# Write your MySQL query statement below
select user_id as buyer_id , join_date , count(buyer_id) as orders_in_2019 
from users join orders 
    on user_id = buyer_id 
where order_date like '2019-%%-%%'
group by user_id 

union all 
(
    select distinct user_id , join_date , 0 
    from users join orders
    where user_id not in (
        select buyer_id 
        from orders 
        where order_date like '2019-%%-%%'
    )
)