-- Example analytics query
SELECT date, SUM(value) as total_value
FROM data.sample
GROUP BY date
ORDER BY date;