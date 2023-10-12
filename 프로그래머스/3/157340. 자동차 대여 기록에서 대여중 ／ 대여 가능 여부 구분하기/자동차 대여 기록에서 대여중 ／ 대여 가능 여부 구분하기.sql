-- 코드를 입력하세요
SELECT car_id, 
max(if('2022-10-16' between start_date and end_date,"대여중","대여 가능")) as availabilty
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc

