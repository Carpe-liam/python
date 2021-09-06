# MySQL Notes

### Database Design:
- DO NOT REPEAT DATA - USE YOUR SPACE EFFICIENTYLY
1. database relations 
	- one to one
	- one to many
	- many to many
2. Three (3) forms of normalization
3. MySQL Workbench
4. RDBMS - relational database management systems
4. Type of data

- by deviding our data into different tables, we make each table good
at storing instances or rows of that data.

---
## Database Relations

### one to one relationship
- IDs = every table should have it's own unique identifier. 
	- will be a column called id, AutoIncrement (AI)
	
- for information that a table could have multiple of, it would be good
to have a separate table & id. this is called a FOREIGN KEY (more on this later):
	- think of the customers table having more than 1 address, it would be good to
	have a separate addresses table with address_id being passed into the
	customer table for each customer.
	- since each address can only belong to a single customer & each customer can
	only have one address (in our table), this is the ONE TO ONE relationship.

- \\other examples\\:
	- Customer & credit card
	- user & email
	- product and image

- |Cliff Note|
	- even w/ 2 separate tables, we can combine the 2 tables into one using SQL 
	down the road; however, this requires the FOREIGN KEY to reference. 

---

### one to many relationship
- think of customers and orders here
- customers can place multiple orders, but each ORDER can only have ONE customer.
	- this is the ONE TO MANY relationship.
- Notice how the foreign key and the id  of the table that we want to combine act 
as the glue. We can join different tables using SQL

- |FOREIGN KEY| => how we join 2 tables so for customers, the foreign key would 
be something like their address_id when being entered onto the customers table and
the customer_id on the customer table would be the primary key. 

- |PRIMARY KEY| => the primary key is the main key that is assigned to the specific
table of values. for customers- it would be the customer_id. if you were on the 
address table, the address_id would be the primary. 

- \\other examples\\:
	- messages & comments
	- States & cities

## many to many relationship
- think of how each order can have many items, and items can (have) up on many orders

- in a many to many relationship, we create a CONNECTOR/JOINER TABLE that has both the 
order_id and the item_id so that we can determine all items in a certain order. 
	- this requires also making an items table that holds id, name, and the 
	description of the item. 
	
- |REMEMBER|: ANYTIME YOU HAVE A MANY-TO-MANY, IT REQUIRES A JOINING TABLE
	
 - \\examples\\:
	- users & interests
	- actors & movies 
	- businesses & cities

---

## Normilization

### the 3 forms of database normalization

- |WHAT IS NORMILIZATION|:
	- a convention for splitting large tables of data into smaller SEPARATE tables with
the primary goal being to not repeat data. 	For example; to update a user's stored email
address - we would simply use it's id rather than just assigning another separate email. 

|TYPE 1|
	- Each column in your table can only have one value:
		- Ex: you should not have an address column in your table that lists the address,
		city, state, and zip all separated by commas. 

|TYPE 2|
	- Each column in your table that is not a key (primary or foreign) must have unique values
		- Ex: if you have a movies table with categories column, you should not have a 
		category repeated more than once. 

|TYPE 3|
	- You cannot have a non-key column that is dependent on another non-key column.
		- Ex: if you have a books table with columns = 'publisher_name' and 'publisher_address',
		the publisher_address and publisher_name should be separated into a separate 
		table and linked to the books with a foreign key. The publisher_address is 
		dependent on the publisher_name and neither column is a key column. 
		
---

## Conventions

### what are the standard conventions and best practices in database design?

1. make the table name PLURAL and all lowercase
2. use 'id' as the primary key
	- should be auto incremented
3. name foreign keys with singular table name_id - when referencing to a primary key
in another table name.
4. use created_at & updated_at as columns for the timestamp in EVERY TABLE

|CLIFF NOTE|
- these conventions become VERY important when working with ORM or Ruby on Rails

## Data Types

### Simple Data Types:

- VARCHAR[number of characters] 
	- used to store non-numeric values that can be up to 255 characters long 
	- will only use the space required for each record stored on the database

- CHAR[number of characters]
	- also used to store non-numeric values, but uses all space for the set number of
	characters regardless of what value is added. 

- INT
	- used to store integers
	- usually used for things like a unique identifier for each table. majority of 
	rows will not exceed 2.1 billion records. INT is good to ue for most normal num 
	values like phone or zip.
	- unsigned(positive numbers only):
		- can store numerical values from 0 to 4294967295
	- signed(postive and negative numbers)
		- can store numerical values from -2147483648 to 2147483647
		
- BIGINT
	- used for columns that would need huge numbers. but if you wanted to store something
	like Facebook's API, you would need it. 
	- unsigned(positive numbers only):
		- can store numerical values from 0 to 18446744073709551615
	- signed(postive and negative numbers)
		- can store numerical values from -9223372036854775808 to 9223372036854775807

- TINYINT
	- good to be used for numbers that are relatively small such as user level identifier 
	where (0- inactive user; 1-active user; & 9-admin). 
	- unsigned 
		- can store values from 0-255
	- signed 
		- can store values from -128 to 127

- FLOAT 
	- used to store floating point numbers (decimal numbers)
	- good use example would be ITEM COST

- TEXT 
	- used to store a large amount of text, like a description, message, or comment. 
	- use for any text VARCHAR is too small to handle
- DATETIME
	- used to store date and time in the format YYYY-MM-DD hh:mm:ss

---

# MySQL Functions

## Text Functions
- CONCAT()
	- SELECT CONCAT ('Mr. ', ' ', first_name, ' ', last_name); AS full_name FROM clients; 
	--:> |THIS WILL CHANGE COLUMN NAME TO WHAT YOU CONCAT|

- CONCAT_WS()
	- SELECT CONCAT_WS(' ' first_name, last_name, 'cool'); AS full_name FROM clients; 
	--:> will put a space between first & last name

- LENGTH()
	- SELECT LENGTH(last_name) AS last_len FROM clients; --:> will return the length 
	of last name as number

- LOWER()
	- SELECT LOWER(first_name) AS first_lowercases FROM clients; --:> will put first name 
	to all lowercase

## Date functions
- HOUR()
	- SELECT HOUR(joined_datetime) AS date_hour FROM clients; --:> will give the hour in 
	24 hour format for each of the 'joined_datetime'
- DAYNAME()
	- SELECT DAYNAME(joined_datetime) AS day_name FROM clients; --:> gives day name
- MONTH()
	- SELECT MONTH(joined_datetime) AS month_number FROM clients; --:> provides month number
- NOW()
	- SELECT NOW() AS right_now; --:> will insert current time
- DATE_FORMAT()
	- SELECT DATE_FORMAT(created_at, '%W %M %e %Y') FROM clients; --:> sets the date
	format to , |%W => weekday name |%m => month[00-12] |%e => month[0-31]|, |%y => year as 2 digits|
	such as Monday Febuary 1 2010

---

# JOINING TABLES
### JOIN
- Find all the clients (first and last name) billing amounts and charged date
	- SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
	- FROM clients
	- JOIN billing ON clients.id = billing.clients_id; 

- list all the domain names and leads (first and last name) for each site
	- SELECT sites.domain_name, leads.first_name, leads.last_name
	- FROM sites
	- JOIN leads ON sites.id = leads.sites_id;

### JOIN ON MULTIPLE TABLES
- Get the names of the clients, their domain names and the first naems of all the leads from those sites.
	- SELECT clients.first_name AS clients_first, clients.last_name, sites.domain_name, leads.first_name AS leads__first
	- FROM clients
	- JOIN sites ON clients.id = sites.clients_id
	- JOIN leads ON sites.id = leads.sites_id;

### LEFT & RIGHT JOIN
- List all of the clients and the sites each client has, even if the client hasn't landed a site yet.
	- SELECT clients.first_name, clients.last_name, sites.domain_name
	- FROM clients
	- LEFT JOIN sites ON clients.id = sites.clients_id;

## GROUPING ROWS
### GROUP BY
- SUM, MIN, MAX, AVG
- Find all the clients (first and last name) and their total billing amounts
	- SELECT clients.first_name, clients.last_name, SUM(billing.amount)
	- FROM clients
	- JOIN billing ON clients.id = billing.clients_id
	- GROUP BY clients.id;

### GROUP CONCAT
- List all the domain names associat ed with each client
	- SELECT GROUP_CONCAT(' ', sites.domain_name) AS domains, clients.first_name, clients.last_name
	- FROM clients
	- JOIN sites ON clients.id = sites.clients_id
	- GROUP BY clients.id;

### COUNT
- Find the total number of leads for each site
	- SELECT COUNT(leads.id), sites.domain_name
	- FROM sites
	- JOIN leads ON sites.id = leads.sites_id
	- GROUP BY sites.id;

--- 

## Difference between JOIN and LEFT JOIN
- While there are other joins, you can make any web application using only JOIN and LEFT JOIN. Don't try and use
others until you really understand LEFT JOIN. Additionally, they are not the same and the output that JOIN and 
LEFT JOIN output are different. 

- |JOIN| => only includes those records that have matches on both sides and omit any records that don't have 
a 'partner' or the foreign key. 

- |LEFT JOIN| => on the other hand, LEFT JOIN will include all records from the FIRST table(aka the 'LEFT' table)
regardless of whether that record has a matching foreign key in the right table to join with.

## QUERY QUESTIONS:
1.	|WHAT QUERY WOULD YOU RUN TO GET ALL TWEETS FROM THE USER ID 1?|
	- SELECT * FROM users
	- LEFT JOIN tweets
	- ON users.id = tweets.user_id
	- WHERE users.id = 1;

2.	|WHAT QUERY WOULD RETURN ALL THE TWEETS THAT THE USER WITH ID 2 HAS TAGGED AS FAVORITES?|
	- SELECT first_name, tweet FROM users
	- LEFT JOIN faves
	- ON users.id = faves.user_id
	- LEFT JOIN tweets
	- ON faves.tweet_id = tweets.id
	- WHERE users.id = 2;

3.	|WHAT QUERY WOULD YOU RUN TO GET ALL THE TWEETS THAT USER W/ ID=2 OR USER WITH ID=1, HAS TAGGED AS FAVE?|
	- SELECT first_name, tweet FROM users
	- LEFT JOIN faves
	- ON users.id = faves.user_id
	- LEFT JOIN tweets
	- ON faves.tweet_id = tweets.id
	- WHERE users.id =1 OR users.id =2;

4.	|WHAT QUERY WOULD YOU RUN TO GET ALL THE USERS THAT ARE FOLLOWNG THE USER WITH ID=1?|
	- SELECT users.first_name AS followed, users2.first_name AS follower
	- FROM users
	- LEFT JOIN follows
	- ON users.id = follows.followed_id
	- LEFT JOIN users AS users2
	- ON users2.id = follows.follower_id
	- WHERE users.id =1;

5.	|WHAT QUERY WOULD YOU RUN TO GET ALL USERS THAT ARE NOT FOLLOWIN GTHE USER WITH ID=2?|
	- SELECT * FROM users
	- WHERE users.id NOT IN (
	- SELECT follower_id FROM follows
	- WHERE followed_id =2)
	- AND users.id !=2;



## Exporting Database Steps
1. click on server tab > Data Export
2. Make sure to export to self contained file
3. Click include schema to include "create databas" line
4. Click on the database/schema you want to export
5. Run export 
6. Now you can copy and paste the file in SQL editor to create database

## Create database from ERD Diagram
1. Ensure MySQL server is running
2. Select Database --> Forward Engineer
3. Confirm credentials are correct and continue
4. IF you need to replace a database you have already created, select "Generate DROP SCHEMA"
otherwise select continue
5. Enter password if promted
6. Select conintue (Top checkbox; Export MySQL Table Objects)
7. Select --> save to file and move saved file to the project folder
8. All the tasks should turn green if succesful, select -> close to continue
9. Select the MySQL connections icon on home page and connect
10. Refresh your schemas if it's not on the list
11. DONE!


