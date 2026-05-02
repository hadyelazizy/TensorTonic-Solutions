-- Write your SQL query here

select u.username, e.experiment_name , e.variant,c.revenue
from users u
join experiment_assignments e on u.id = e.user_id
join conversions c on u.id = c.user_id
order by e.experiment_name asc, c.revenue desc,u.username asc;