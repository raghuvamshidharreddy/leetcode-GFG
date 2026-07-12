# Write your MySQL query statement below
#select manager as Name From 
select manager as name 
From
    (select e1.name as manager,
            e1.department as department,
            e2.managerId as manId
            from Employee e1
                join Employee e2 where e1.id=e2.managerid
                group by manId having count(manId)>=5
    ) as sub;