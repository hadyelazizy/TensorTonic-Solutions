-- Write your SQL query here
select username, session_count,
    CASE 
        WHEN session_count >= 50 THEN 'Power' 
        WHEN session_count >= 10 THEN 'Casual' 
        ELSE 'Dormant'
    END as activity_level,
    CASE 
        WHEN platform in ('ios','android') THEN 'Mobile'
        WHEN platform in ('web','desktop') THEN 'Desktop'
    ELSE 'Other'
    END as platform_type 

from user_sessions

order by CASE 
        WHEN session_count >= 50 THEN 1
        WHEN session_count >= 10 THEN 2
        ELSE 3
    END ASC, username ASC;
