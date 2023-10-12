SELECT u.user_id, u.nickname, sum(b.price) as total_sales
from USED_GOODS_BOARD b, USED_GOODS_USER u
where b.status = "done" and u.user_id = b.writer_id
group by user_id having total_sales >= 700000
order by total_sales 