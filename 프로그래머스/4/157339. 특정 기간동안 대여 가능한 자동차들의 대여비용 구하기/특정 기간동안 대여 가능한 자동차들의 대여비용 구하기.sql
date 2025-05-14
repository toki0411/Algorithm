WITH A AS(
    SELECT * from CAR_RENTAL_COMPANY_CAR 
    where car_type in ( '세단', 'SUV' )
),
B AS (
    SELECT H.CAR_ID, A.CAR_TYPE, A.DAILY_FEE from CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    JOIN A on H.CAR_ID = A.CAR_ID
    where H.car_id not in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                            where END_DATE >= '2022-11-01' 
                           AND START_DATE <= '2022-12-01')
    group by car_id
),
C AS (
    SELECT CAR_TYPE, MAX(DISCOUNT_RATE) as DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE DURATION_TYPE <> '90일 이상'
    AND CAR_TYPE IN  ( '세단', 'SUV' ) 
    GROUP BY CAR_TYPE 
)
select B.CAR_ID, B.CAR_TYPE, floor((B.daily_fee * 30) * ((100 - C.discount_rate)/100)) as FEE from B,C
WHERE C.car_type = B.car_type and floor((B.daily_fee * 30) * ((100 - C.discount_rate)/100)) >= 500000 AND floor((B.daily_fee * 30) * ((100 - C.discount_rate)/100)) < 2000000
order by fee desc, B.car_type, B.CAR_ID desc
;