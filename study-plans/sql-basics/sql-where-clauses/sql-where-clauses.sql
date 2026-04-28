-- Write your SQL query here


select name,salary 
    From employees 
    where (salary>70000) AND (department = 'Engineering' or department = 'Marketing');