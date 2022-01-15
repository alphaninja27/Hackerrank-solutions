SELECT ROUND(X.LAT_N, 4)
FROM STATION AS X, STATION AS Y /*Self join*/
GROUP BY X.LAT_N
HAVING SUM(SIGN(1-SIGN(Y.LAT_N - X.LAT_N)))/COUNT(X.LAT_N) > 0.5
LIMIT 1;