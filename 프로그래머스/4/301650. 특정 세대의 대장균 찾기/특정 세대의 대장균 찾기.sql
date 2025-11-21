with a as (
    select id
    from ecoli_data
    where parent_id is null
),
b as (
    select e.* 
    from ecoli_data e
    join a on a.id = e.PARENT_ID
),
c as (
    select e.*
    from ecoli_data e
    join b on b.id = e.parent_id
)
select c.id from c
order by id;