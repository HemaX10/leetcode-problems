# Write your MySQL query statement below
select round(sum(ins1.tiv_2016),2) as tiv_2016
from insurance ins1 join insurance ins2
on ins1.pid = ins2.pid
where ins1.tiv_2015 in (
    select tiv_2015 from insurance where pid != ins1.pid
) and ins1.pid in (
    select pid from insurance group by lat , lon having count(pid) = 1
)


