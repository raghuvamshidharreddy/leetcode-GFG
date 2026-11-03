# Write your MySQL query statement below
with temp as(select f.id,f.name employee,salary,dense_rank() over(partition by departmentid order by Salary desc) as rnk,d.name as department
from Employee f join Department d on d.id=f.departmentid)
select Department,employee,salary from temp where rnk<=3;