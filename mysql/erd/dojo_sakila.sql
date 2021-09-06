-- 1
SELECT city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM city
JOIN address
ON city.city_id = address.city_id
JOIN customer
ON address.address_id = customer.address_id
WHERE city.city_id = 312;

-- 2
SELECT film.film_id, film.title, film.release_year, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category 
ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

-- 3
SELECT actor.actor_id, CONCAT_WS(" ", actor.first_name, actor.last_name) AS actor_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor 
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- 4
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address
ON customer.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id
WHERE customer.store_id =1 AND (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459);  

-- 5

SELECT film.title, film.description, film.release_year, film.rating, film.special_features 
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor 
ON film_actor.actor_id = actor.actor_id
WHERE film.rating ="G" AND film_actor.actor_id =15 AND film.special_features = "Behind the Scenes";

-- 6 
SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(" ",actor.first_name, actor.last_name) AS actor_name
FROM film
JOIN film_actor 
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- 7
SELECT film.title , film.description, film.release_year, film.rating, film.special_features, category.name, payment.amount
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
LEFT JOIN inventory
ON film.film_id = inventory.film_id
LEFT JOIN rental
ON inventory.inventory_id = rental.inventory_id
LEFT JOIN payment
ON rental.rental_id = payment.rental_id
WHERE payment.amount = 2.99 AND category.name = "DRAMA"
GROUP BY (film.title);


-- 8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, CONCAT_WS(" ",actor.first_name, actor.last_name) AS actor_name
FROM film 
JOIN film_actor 
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = "Action" AND actor.first_name = "SANDRA" AND actor.last_name = "KILMER";

SELECT CONCAT_WS(" ",actor.first_name, actor.last_name) AS actor_name FROM actor;

SELECT film_category.category_id FROM film_category;
SELECT * FROM category;
SELECT * FROM city;
SELECT * FROM customer;
SELECT * FROM address;