-- Write your SQL query here
select category, count(*) as total_sales, sum(amount) as total_revenue, avg(discount) as avg_discount
from sales
group by category
order by total_revenue desc, category asc;