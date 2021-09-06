INSERT INTO dojos (name)
VALUES("alpha"), ("brovo"), ("charli");

DELETE FROM dojos
WHERE name = "alpha";
DELETE FROM dojos
WHERE name = "brovo";
DELETE FROM dojos
WHERE name ="charli";

INSERT INTO dojos (name)
VALUES("delta"), ("epsilon"), ("foxtrot");

--  DOJO 4
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(1, "Monty", "Python", 18, 4);
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(2, "Benedict", "Cucumber-patch", 255, 4);
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(3, "Karma", "Nova", 26, 4);

-- DOJO 5
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(4, "DJ", "Slim", 6, 5);
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(5, "Private", "Donut", 23, 5);
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(6, "Optimus", "Prime", 8472, 5);

-- DOJO 6
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(7, "G.I", "Joe", 56, 6);
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(8,"Naruto", "Uzimake", 17, 6);
INSERT INTO ninjas (id, first_name, last_name, age, dojo_id)
VALUES(9, "Kakashi", "Hakate", 48, 6);

SELECT * FROM dojos
JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;

SELECT * FROM dojos
JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 6;

SELECT first_name, last_name, dojo_id FROM ninjas
WHERE ninjas.id = 9;

SELECT * FROM dojos;
SELECT * FROM ninjas;