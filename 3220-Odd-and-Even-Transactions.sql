# Write your MySQL query statement below
with tableSumEvenOddAmount 
as (
select transaction_date , case 
                        when amount % 2 = 0 
                        then 0 
                        else amount 
                        end as odd_sum ,
                        case 
                        when amount % 2 = 0 
                        then amount 
                        else 0 
                        end as even_sum
from transactions )

select transaction_date , sum(odd_sum) as odd_sum , sum(even_sum) as even_sum
from tableSumEvenOddAmount
group by transaction_date 
order by transaction_date  asc