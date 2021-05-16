--create inital tables for data population

CREATE TABLE forest_area
	(
	id SERIAL PRIMARY KEY,
	country_code VARCHAR(50),
	country_name VARCHAR(50),
	year INTEGER,
	forest_area_sqkm NUMERIC
	);
	
CREATE TABLE land_area
	(
	id SERIAL PRIMARY KEY,
	country_code VARCHAR (50),
	country_name VARCHAR (50),
	year INTEGER,
	total_area_sq_mi NUMERIC
	);
	
CREATE TABLE regions
	(
	id SERIAL PRIMARY KEY,
	country_name VARCHAR (50),
	country_code VARCHAR (50),
	income_group VARCHAR (50),
	region VARCHAR (50)		
	);