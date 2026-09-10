# Write your MySQL query statement below
-- With unbanned_users as(select users_id from users where banned='No')
select 
    request_at as  Day ,
    round(count(case when status in('cancelled_by_driver','cancelled_by_client') Then status End)/
    count(status),2) as 'Cancellation Rate'
From Trips
Where 
    client_id in(select users_id from users where banned='No') And
    driver_id in (select users_id from users where banned='No') and 
    request_at between "2013-10-01" And "2013-10-03"  
group by request_at;