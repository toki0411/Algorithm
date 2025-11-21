with A as (
SELECT host_id from 
PLACES 
group by host_id having count(id) > 1)
select B.* from places B
join A on B.host_id = A.host_id
order by B.id;