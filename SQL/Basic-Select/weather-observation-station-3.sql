/*
Enter your query here.
*/

SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID,2) = 0;