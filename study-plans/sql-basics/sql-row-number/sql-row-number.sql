-- Write your SQL query here

select username,segment,engagement_score,
row_number() over (partition by segment order by engagement_score desc,username asc) as activity_rank
from user_activity
order by segment asc,activity_rank asc;