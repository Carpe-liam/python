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
# Database Relations

## one to one relationship
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

## one to many relationship
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

# MySQL HW ERD Notes

## Self Join
- you can self join a table like a user with friendships [see assignment] and just use
2 1:n arrows going from friendships {the thing you've got many of} to the users table

