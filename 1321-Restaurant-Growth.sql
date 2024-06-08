select  visited_on, amount , average_amount 
from 
    (select visited_on, sum(sum(amount)) over(order by visited_on RANGE BETWEEN INTERVAL 6 DAY   PRECEDING AND CURRENT Row) as amount , round(avg(sum(amount)) over(order by visited_on RANGE BETWEEN INTERVAL 6 DAY   PRECEDING AND CURRENT Row) , 2) as average_amount , row_number() over(order by visited_on) as rn
    from customer
    group by visited_on
    order by visited_on  ) as newtable
where rn > 6 