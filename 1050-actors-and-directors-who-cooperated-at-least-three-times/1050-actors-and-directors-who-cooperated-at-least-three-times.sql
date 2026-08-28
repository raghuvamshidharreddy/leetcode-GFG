# Write your MySQL query statement below
select actor_id,director_id FROM
ActorDirector group by director_id,actor_id Having count(actor_id)>=3 and count(director_id)>=3 ;
