# Write your MySQL query statement below
select event_day as 'day' , emp_id , sum(totalTime) as total_time
from(
select * , out_time - in_time as totalTime
from employees ) as newtable1
group by emp_id , event_day
