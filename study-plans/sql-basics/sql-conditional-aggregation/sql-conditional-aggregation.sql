-- Write your SQL query here

select department, count(*) as total_tickets, 
    sum(case when status = 'open' then 1 else 0 end) as open_count,
    sum(case when status = 'in_progress' then 1 else 0 end) as in_progress_count,
    sum(case when status = 'closed' then 1 else 0 end) as closed_count

from tickets
group by department
order by total_tickets desc, department asc;

    