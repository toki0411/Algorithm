with A as (
    select writer_id, count(board_id) as cnt
    from USED_GOODS_BOARD
    group by writer_id
), B as (
    select user_id, nickname, CONCAT(city, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소', concat(substring(TLNO, 1,3), '-', substring(TLNO,4,4), '-', substring(TLNO,8,4)) as '전화번호'
    from USED_GOODS_USER
)
select B.* 
from B
join A on A.writer_id = B.user_id
where A.cnt >= 3
order by B.user_id desc;