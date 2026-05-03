-- Write your SQL query here

select round(avg(daily_count),2) as avg_daily_orders,
    round(avg(daily_revenue),2) as avg_daily_revenue, 
    max(daily_count) as busiest_day_orders
from(
        select order_date,
            count(*) as daily_count, 
            sum(amount) as daily_revenue
    from orders
    group by order_date
);