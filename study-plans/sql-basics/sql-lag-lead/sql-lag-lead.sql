-- Write your SQL query here
select month,revenue,LAG(revenue,1,0) OVER (order by month) as prev_revenue,
revenue - prev_revenue as revenue_change
from monthly_revenue 
order by month asc;