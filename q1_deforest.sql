--New file.
--According to the World Bank, the total forest area of the world was 41,282,694.9 sqkm in 1990. 
--As of 2016, the most recent year for which data was available, 
--That number had fallen to 39,958,245.9 sqkm, a loss of 132,449 sqkm, or -3% of the world's sqkm which is sizable

SELECT * FROM forest_area;

WITH t1 AS
	(SELECT
	year,
	country_name, 
	forest_area_sqkm AS forest_1990
	FROM forest_area
	WHERE year = '1990'
	AND country_name = 'World'),
t2 AS
	(SELECT
	year,
	country_name, 
	forest_area_sqkm AS forest_2016
	FROM forest_area
	WHERE year = '2016'
	AND country_name = 'World')
SELECT 
t1.forest_1990,
t2.forest_2016,
t1.forest_1990-t2.forest_2016 AS difference_in_sqkm,
(t2.forest_2016/t1.forest_1990*100)-100 AS percent_difference_in_sqkm
FROM t1
JOIN t2
ON t1.country_name=t2.country_name;