with A as (
    select id, size_of_colony, rank() over (order by size_of_colony desc) as ranking
    from ECOLI_DATA
), B as (
    select count(id) as cnt
    from ECOLI_DATA
)
select A.ID, 
case when (A.ranking / B.cnt) * 100 <= 25 then 'CRITICAL'
     when (A.ranking / B.cnt) * 100 <= 50 then 'HIGH'
     when (A.ranking / B.cnt) * 100 <= 75 then 'MEDIUM'
     when (A.ranking / B.cnt) * 100 <= 100 then 'LOW'
end as colony_name
from A, B
order by A.ID;