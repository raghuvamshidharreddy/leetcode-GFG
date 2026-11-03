# Write your MySQL query statement below
with user as
(
    select u.name, count(u.user_id) as no_of_reviews
    from
    users u
    join movierating mr on
    mr.user_id=u.user_id
    join movies m on
    mr.movie_id=m.movie_id
    group by u.name
    order by no_of_reviews desc,u.name limit 1
),
movie as
(
    select m.title, avg(mr.rating) as average_rating
    from
    users u
    join movierating mr on
    mr.user_id=u.user_id
    join movies m on
    mr.movie_id=m.movie_id
    where year(mr.created_at)=2020 and month(mr.created_at)=2 
    group by m.title
    order by average_rating desc,m.title limit 1
)
select name as results from user
union all
select title from movie;