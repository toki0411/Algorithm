with A as (
    select LOCATION1, LOCATION2, YEAR(YM) as YM, PM_VAL1, PM_VAL2
    from AIR_POLLUTION
    where location2 = '수원'
)
select YM as YEAR, round(avg(pm_val1),2) as PM10, round(avg(pm_val2),2) as 'PM2.5'
from A
group by YM
order by YM