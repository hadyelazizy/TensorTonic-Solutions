-- Write your SQL query here

select account,txn_date,amount, 
    SUM(amount) over (
    PARTITION BY account 
    ORDER BY txn_date asc , id asc
    ) as running_total
from transactions
order by account asc, txn_date asc, id asc;