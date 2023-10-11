SELECT category, sum(s.sales) as total_sales
from book b join book_sales s 
on b.book_id = s.book_id
where s.sales_date between '2022-01-01' and '2022-01-31'
group by category 
order by category


