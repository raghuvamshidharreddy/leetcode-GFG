# Write your MySQL query statement below
with pos as(select 
    patient_id,
    min(test_date) td
from covid_tests
where result='Positive'
group by patient_id)
, neg as
(select 
    pos.patient_id,
    p.patient_name,
    p.age,
    DateDiff(min(ct.test_date),pos.td)as recovery_time
from covid_tests ct
join pos on
pos.patient_id=ct.patient_id
join patients p on
pos.patient_id=p.patient_id
where ct.result='Negative' and pos.td<ct.test_date
group by patient_id
order by datediff(min(ct.test_date),pos.td),p.patient_name)

select * from neg;
