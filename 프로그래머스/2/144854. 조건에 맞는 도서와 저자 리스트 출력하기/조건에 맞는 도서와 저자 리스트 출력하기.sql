SELECT b.book_id, a.author_name, 
date_format(b.published_date, '%Y-%m-%d') as published_date
from book b join author a 
on b.category = '경제' and a.author_id = b.author_id
order by published_date
