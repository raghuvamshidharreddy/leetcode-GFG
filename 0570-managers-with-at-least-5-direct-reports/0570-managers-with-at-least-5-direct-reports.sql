# Write your MySQL query statement below
#select manager as Name From
select name from employee
where id in (
select managerid from employee
group by managerid
having count(managerid)>=5);