-- Write your SQL query here

select username, signup_date, 
    EXTRACT(YEAR FROM signup_date) as signup_year,
    EXTRACT(MONTH FROM signup_date) as signup_month,
    EXTRACT(QUARTER FROM signup_date) as signup_quarter,
    DATE_TRUNC('month',signup_date) as cohort_month

from signups
order by signup_date asc, username asc;