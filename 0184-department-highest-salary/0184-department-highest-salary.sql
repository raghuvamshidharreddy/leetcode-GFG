# Write your MySQL query statement below
select Department,Employee,Salary 
from
    (select e.departmentId,e.name as Employee,e.salary as Salary,d.name as department,
    dense_rank() over(partition by d.name order by salary desc) as rnk
    from Employee e
    Left Join department d on  e.departmentId=d.id ) as sub
where rnk=1;