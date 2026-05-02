-- Write your SQL query here

select u.username , COALESCE(r.username,'organic') as referrer_name
from user_referrals u 
left join user_referrals r on u.referred_by = r.id
ORDER BY u.username ASC;

