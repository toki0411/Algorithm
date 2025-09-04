with A as (
    select id, fish_type, 
    case when 
        length is null
        then 10 
        else length
        end as length
    from fish_info
), 
B as (
    select count(id) as FISH_COUNT, avg(length) as AVG_LENGTH, max(length) as MAX_LENGTH, fish_type
    from A
    group by fish_type
)
select FISH_COUNT, MAX_LENGTH, FISH_TYPE 
from B
where avg_length >= 33
order by FISH_TYPE ;

