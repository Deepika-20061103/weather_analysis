
CREATE DATABASE IF NOT EXISTS weather_db;
USE weather_db;

-- 1. Display all weather records
SELECT * FROM weather;

-- 2. Total number of records
SELECT COUNT(*) AS total_records FROM weather;

-- 3. Average temperature
SELECT ROUND(AVG(temperature), 2) AS average_temperature
FROM weather;

-- 4. Maximum temperature
SELECT MAX(temperature) AS maximum_temperature
FROM weather;

-- 5. Minimum temperature
SELECT MIN(temperature) AS minimum_temperature
FROM weather;

-- 6. Total rainfall
SELECT SUM(rainfall) AS total_rainfall
FROM weather;

-- 7. City-wise average temperature
SELECT city, ROUND(AVG(temperature), 2) AS avg_temperature
FROM weather
GROUP BY city;

-- 8. Weather condition count
SELECT weather_condition, COUNT(*) AS total_days
FROM weather
GROUP BY weather_condition;

-- 9. City-wise average rainfall
SELECT city, ROUND(AVG(rainfall), 2) AS avg_rainfall
FROM weather
GROUP BY city;

-- 10. Highest rainfall day
SELECT weather_date, city, rainfall
FROM weather
ORDER BY rainfall DESC
LIMIT 1;

-- 11. Display rainy days
SELECT * FROM weather
WHERE weather_condition = 'Rainy';

-- 12. Temperature in descending order
SELECT city, temperature
FROM weather
ORDER BY temperature DESC;

