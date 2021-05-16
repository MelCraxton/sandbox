--this was done to create inital tables for data population
-- these are the main tables used in the course project

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

-- fix mismatched columns

ALTER TABLE region
RENAME COLUMN income_group TO regions;

ALTER TABLE region
RENAME COLUMN region TO income_group;

ALTER TABLE regions
RENAME COLUMN regions TO region;