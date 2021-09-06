INSERT INTO authors (name)
VALUES("Jane Austen"), ("Emily Dickinson"), ("Fyodor Dosteoevsky"), ("William Shakespeare"), ("Lau Tzu");

INSERT INTO books (title, num_of_pages)
VALUES ("C Sharp", 544), (" Java", 208), ("Python", 309), ("PHP", 823), ("Ruby", 582);

UPDATE books
SET books.title = "C#"
WHERE books.title = "C Sharp";

UPDATE authors
SET authors.name = "Bill Shakespeare"
WHERE authors.name = "William Shakespeare";

INSERT INTO favorites (favorites.book_id, favorites.author_id)
VALUES (1, 1), (2, 1);
INSERT INTO favorites (favorites.book_id, favorites.author_id)
VALUES (1, 2), (2, 2), (3,2);
INSERT INTO favorites (favorites.book_id, favorites.author_id)
VALUES (1, 3), (2, 3), (3, 3), (4, 3);
INSERT INTO favorites (favorites.book_id, favorites.author_id)
VALUES (1, 4), (2, 4), (3, 4), (4, 4), (5, 4);

SELECT authors.name FROM authors
JOIN favorites
ON authors.id = favorites.author_id
WHERE favorites.book_id = 3;

DELETE FROM favorites
WHERE favorites.author_id = 2;

INSERT INTO favorites (favorites.book_id, favorites.author_id)
VALUES (2,5);

SELECT title FROM books
JOIN favorites
ON books.id = favorites.book_id
JOIN authors
ON favorites.author_id = authors.id
WHERE favorites.author_id = 3;

SELECT name FROM authors
JOIN favorites
ON authors.id = favorites.author_id
JOIN books
ON favorites.book_id = books.id
WHERE books.id =5;


SELECT * from authors;
SELECT * from books;
SELECT * from favorites;