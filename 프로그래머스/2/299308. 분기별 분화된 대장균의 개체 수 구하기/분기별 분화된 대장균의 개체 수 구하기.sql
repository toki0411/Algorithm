with A as (
    select ID, DIFFERENTIATION_DATE, 
    case when month(DIFFERENTIATION_DATE) in ("01", "02", "03") then "1Q"
    when month(DIFFERENTIATION_DATE) in ("04", "05", "06") then "2Q"
    when month(DIFFERENTIATION_DATE) in ("07", "08", "09") then "3Q"
    when month(DIFFERENTIATION_DATE) in ("10", "11", "12") then "4Q"
    end as QUARTER 
from ecoli_data
)
select A.QUARTER, count(*) as ECOLI_COUNT
FROM A
GROUP BY QUARTER
ORDER BY QUARTER;