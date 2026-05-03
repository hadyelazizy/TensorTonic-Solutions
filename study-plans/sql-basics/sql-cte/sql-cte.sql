-- Write your SQL query here

with order_stats as (

    select customer,count(*) as order_count, sum(amount) as total_spent
    from orders
    group by customer
)

select customer, order_count,total_spent
from order_stats
where order_count>1
order by total_spent desc, customer asc;