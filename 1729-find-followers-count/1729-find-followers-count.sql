/* Write your PL/SQL query statement below */
select
     user_id,
     count(distinct follower_id) as followers_count
From followers
group by user_id
order by user_id asc;