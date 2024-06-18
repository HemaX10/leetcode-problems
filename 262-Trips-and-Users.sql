# Write your MySQL query statement below
select request_at as Day, round(avg(casee),2) as 'Cancellation Rate' 
from 
(
select request_at , id , case when 
    status = 'cancelled_by_driver' or status = 'cancelled_by_client' then 1.0 
    else 0.0 
    end as casee
from trips 
    inner join users user1
        on client_id  = user1.users_id and user1.role = 'client'
    inner join users user2
        on driver_id  = user2.users_id and user2.role = 'driver'  
where
    request_at in ('2013-10-02' , '2013-10-03' , '2013-10-01')
    and user1.banned = 'No'
    and user2.banned = 'No'
) as newtable
group by request_at