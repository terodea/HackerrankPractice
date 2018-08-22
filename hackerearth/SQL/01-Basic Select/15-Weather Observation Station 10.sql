SELECT DISTINCT City
FROM Station
WHERE REGEXP_LIKE(City, '[^aeiou]$');
