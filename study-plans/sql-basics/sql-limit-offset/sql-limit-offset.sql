-- Write your SQL query here


select product, revenue, sale_date
    from sales 
    order by revenue DESC, sale_date ASC
    limit 3 offset 1;  