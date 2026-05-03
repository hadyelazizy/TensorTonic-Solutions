-- Write your SQL query here

select p.name,p.price, round(p.price-(select avg(price) from products),2) as vs_avg 
from products p
WHERE p.id IN (SELECT product_id FROM sales)
order by vs_avg  desc, p.name asc;
