SELECT months * salary AS earnings, COUNT(*) 
FROM Employee 
GROUP BY 1  -- Group by 1 means to group by the first column
ORDER BY earnings DESC
LIMIT 1;
