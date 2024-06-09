# Write your MySQL query statement below
select stock_name , sum(newPrice) as capital_gain_loss
from (
select * , case when operation = 'Buy' then price * -1
                    else price end as newPrice
from stocks ) as newtable
group by stock_name