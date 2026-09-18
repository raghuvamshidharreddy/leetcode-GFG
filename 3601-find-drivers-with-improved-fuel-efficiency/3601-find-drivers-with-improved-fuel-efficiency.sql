# Write your MySQL query statement below
with temp as(
    select 
        driver_id,
        trip_date,
        distance_km/fuel_consumed as mil
    from trips  
)
,first_half as (
    
    select 
        d.driver_id,
        d.driver_name,
        avg(mil) as first_half_avg
    from drivers d
    join temp t on 
        d.driver_id=t.driver_id
    where 
        Month(trip_date) in (1,2,3,4,5,6)
    group by d.driver_id),
second_half as(
    select 
        d.driver_id,driver_name,
        avg(mil) as second_half_avg
    from drivers d
    join temp t on 
        d.driver_id=t.driver_id
    where 
        Month(trip_date) in(7,8,9,10,11,12)
    group by d.driver_id)

select 
    f.driver_id,
    f.driver_name,
    round(f.first_half_avg,2) as first_half_avg,
    round(s.second_half_avg,2) as second_half_avg,
    round(s.second_half_avg-f.first_half_avg,2) as efficiency_improvement
from first_half f join
second_half s on f.driver_id=s.driver_id
where round(s.second_half_avg-f.first_half_avg,2)>0
order by efficiency_improvement desc , f.driver_name;