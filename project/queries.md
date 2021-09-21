SELECT * FROM users;
SELECT * FROM tasks;
SELECT * FROM notes;

INSERT INTO users (first_name, last_name, username, email, password)
VALUES ("Alex", "Tyler", "Karma", "karma@mal.com", "1234qwer");

INSERT INTO users (first_name, last_name, username, email, password)
VALUES ("Butters", "Boi", "Bubbas", "bubbas@mal.com", "buttersboi");

INSERT INTO tasks (user_id, title, description, importance, completed, due_by)
VALUES (2, "Feed Me", "Get alex to feed me every 20 seconds", 1, 0, "2021-09-22" );

INSERT INTO tasks (user_id, title, description, importance, completed, due_by)
VALUES (1, "Ignore Butters", "Refuse butters any food other than his expected meal times or he will get fat", 3, 0, "2021-09-25" );

SELECT CONCAT_WS(" ", users.first_name, users.last_name) AS name, tasks.title, tasks.description, tasks.created_at FROM users
LEFT JOIN tasks 
ON users.id = tasks.user_id
ORDER BY tasks.importance and tasks.created_at ASC;

INSERT INTO notes (task_id, content)
VALUES (1, "Break into snack drawer when alex is sleeping");

INSERT INTO notes (task_id, content)
VALUES (2, "Lock snack drawer at night");

SELECT CONCAT_WS(" ", users.first_name, users.last_name) AS name, tasks.title, tasks.description, notes.content, tasks.created_at FROM users
LEFT JOIN tasks 
ON users.id = tasks.user_id
LEFT JOIN notes
ON tasks.id = notes.task_id
ORDER BY tasks.importance and tasks.created_at ASC;