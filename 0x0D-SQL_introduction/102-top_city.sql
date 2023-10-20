-- Display the top 3 cities in terms of temperature averages
-- Syntax below selects the top three cities by temperature average
SELECT city, AVG(value) AS avg_temp 
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
