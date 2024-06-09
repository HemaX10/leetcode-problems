# Write your MySQL query statement below
select id , case when p_id is Null then 'Root' 
            when id not in (
                select p_id from Tree where p_id
            ) then 'Leaf'
            else 'Inner' end as type
from Tree