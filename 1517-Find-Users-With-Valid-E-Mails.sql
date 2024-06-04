# Write your MySQL query statement below
select * 
from users 
where mail regexp '^[a-zA-Z][0-9a-zA-Z_.-]*@leetcode\\.com$'