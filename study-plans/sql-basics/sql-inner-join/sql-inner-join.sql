-- Write your SQL query here


select e.name,e.salary,d.dept_name
from employees e
inner join departments d on e.dept_id  = d.id
ORDER BY e.name ASC;

