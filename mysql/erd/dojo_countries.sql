SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages 
ON countries.code = languages.country_code
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.id) AS num_cities
FROM countries JOIN cities
ON countries.code = cities.country_code
GROUP BY (cities.country_code) 
ORDER BY num_cities DESC;

SELECT cities.name, cities.population, cities.country_id
FROM countries
JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC;


SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages 
ON countries.id = languages.country_id
WHERE languages.percentage > 89.0
ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities
ON countries.id = cities.country_id
WHERE cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT countries.region, COUNT(countries.id) AS num_countries
FROM countries
GROUP BY countries.region
ORDER BY num_countries DESC;

SELECT * FROM countries;
SELECT * FROM languages;
SELECT * FROM city;