# Write your MySQL query statement below
select * from (
select name , sum(amount) as balance 
from users usee join Transactions trans
    on usee.account = trans.account
group by trans.account ) as newtable 
where balance > 10000