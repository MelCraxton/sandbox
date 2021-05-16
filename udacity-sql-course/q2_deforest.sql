--In 1990, the percent of the total land area of the world designated as forest was 32.42%. 
--The region with the highest relative forestation was Latin America and Caribbean with 51.03%, 
-- The region with the lowest relative forestation was Middle East and North Africa, with 1.78% 
forestation.

WITH t1 AS
(SELECT
regions.region,
ROUND(SUM(land_area.total_area_sq_mi*2.59),2) AS total_area_mi,
ROUND(SUM(forest_area.forest_area_sqkm),2),
ROUND(SUM(forest_area.forest_area_sqkm)/SUM(land_area.total_area_sq_mi*2.59),2)*100 AS total_percent_1990
FROM regions
JOIN forest_area
ON regions.country_name=forest_area.country_name
JOIN land_area
ON land_area.country_name=regions.country_name
WHERE forest_area.year = 1990
GROUP BY 1
ORDER BY 4 DESC),
t2 AS
(SELECT
regions.region,
ROUND(SUM(land_area.total_area_sq_mi*2.59),2) AS total_area_mi,
ROUND(SUM(forest_area.forest_area_sqkm),2),
ROUND(SUM(forest_area.forest_area_sqkm)/SUM(land_area.total_area_sq_mi*2.59),2)*100 AS total_percent_2016
FROM regions
JOIN forest_area
ON regions.country_name=forest_area.country_name
JOIN land_area
ON land_area.country_name=regions.country_name
WHERE forest_area.year = 2016
GROUP BY 1
ORDER BY 4 DESC)
SELECT
t1.region,
t1.total_percent_1990,
t2.total_percent_2016
FROM t1
JOIN t2
ON t1.region = t2.region;