SELECT * FROM users;
SELECT * FROM questions;
SELECT * FROM answers;

INSERT INTO questions (user_id, title, description, answered)
VALUES (1, "What is the meaning of life?", "While the meaning of life is ubiquitous for the search for one's self. What does it mean to you?", "No");

INSERT INTO questions (user_id, title, description, answered)
VALUES (2, "Star Wars - Disney movies. Good or Bad?", "", "Yes");

INSERT INTO questions (user_id, title, description, answered)
VALUES (1,"How to get good at coding?", "I recently started coding and am looking to take it further, what should i do?", "No");


SELECT questions.*, users.username FROM questions 
LEFT JOIN users
ON questions.user_id = users.id
ORDER BY questions.created_at DESC;

SELECT questions.*, answers.content, answers.created_at FROM questions
LEFT JOIN users
ON questions.user_id = users.id
LEFT JOIN answers
ON questions.id = answers.question_id
WHERE questions.id = 5;

INSERT INTO answers (user_id, question_id, content)
VALUES (2, 2, "pretty shite!") ;




SELECT users.username AS owner,  answers.*FROM answers
LEFT JOIN users
ON answers.user_id = users.id
JOIN questions
ON users.id = questions.user_id
WHERE answers.question_id = 2;











