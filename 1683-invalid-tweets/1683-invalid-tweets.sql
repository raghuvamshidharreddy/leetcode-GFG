# Write your MySQL query statement below
select tweet_id
From tweets
where length(content)>15;