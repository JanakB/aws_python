-- -- -- show databases;
-- -- -- create table unlimited.Aws (`name` char(30), `Age` varchar(10), `Address` varchar(20));
-- -- show tables;
-- -- -- alter table Unlimited.aws rename column Address to contact;

-- -- use unlimited;

-- -- create table chort3 (
-- --     First_Name varchar(15),
-- --     Last_Name varchar(20),
-- --     Address char(40),
-- --     contact_No int,
-- --     Age int
-- -- );
-- -- show variables like 'secure_file_priv'
-- -- show tables;

-- -- SELECT * from chort3;

-- -- insert into chort3 values("ram","khadka","ktm",9872,34),("hari","hari","pokhara",7262,65),("shyam","singh","butwal",28372,54)

-- -- SElect * from chort3;

-- -- insert into chort3 (First_Name,Age) values("anant",45)

-- -- SElect * from chort3;

-- -- Alter table chort3 rename column Last_Name to Sir_Name ---rename command

-- -- SElect * from chort3;

-- -- alter table chort3 drop column Sir_Name  ---drop column

-- create table staffs1(
--     EMPLOYEE_ID int,
--     FIRST_NAME varchar(20),
--     Last_Name varchar(20),
--     email varchar(40),
--     phone int)

-- SElect * from staffs1;

-- load data infile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\demo.csv.txt"
-- into table staffs1
-- fields terminated by ','
-- ignore 1 rows;


-- SELECT * from staffs1;

-- SELECT EMPLOYEE_ID,FIRST_NAME,Last_Name,email,phone
-- into outfile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\demo.csv"
-- fields terminated by '#'
-- from staffs1;

create database world;

use world;

CREATE TABLE orgdata (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  countrycode VARCHAR(3),
  salary DECIMAL(10, 2),
  phone_no VARCHAR(20)
);

-- Inserting sample data
INSERT INTO orgdata (id, name, countrycode, salary, phone_no)
VALUES
  (1, 'John', 'USA', 5000.00, '123-456-7890'),
  (2, 'Alice', 'CAN', 4500.00, '987-654-3210'),
  (3, 'Michael', 'USA', 6000.00, '555-123-4567'),
  (4, 'Sophia', 'CAN', 5500.00, '444-555-6666'),
  (5, 'David', 'USA', 5200.00, '888-999-0000'),
  (6, 'Olivia', 'CAN', 4700.00, '777-888-9999'),
  (7, 'William', 'USA', 5100.00, '111-222-3333'),
  (8, 'Emma', 'CAN', 4800.00, '222-333-4444'),
  (9, 'Alexander', 'USA', 5300.00, '333-444-5555'),
  (10, 'Ava', 'CAN', 4900.00, '444-555-6666'),
  (11, 'Daniel', 'USA', 5500.00, '555-666-7777'),
  (12, 'Isabella', 'CAN', 5200.00, '666-777-8888'),
  (13, 'Matthew', 'USA', 6000.00, '777-888-9999'),
  (14, 'Mia', 'CAN', 4700.00, '888-999-0000'),
  (15, 'Ethan', 'USA', 5100.00, '999-000-1111'),
  (16, 'Charlotte', 'CAN', 4800.00, '000-111-2222'),
  (17, 'Andrew', 'USA', 5500.00, '111-222-3333'),
  (18, 'Sophie', 'CAN', 4900.00, '222-333-4444'),
  (19, 'Joseph', 'USA', 5300.00, '333-444-5555'),
  (20, 'Grace', 'CAN', 5000.00, '444-555-6666'),
  (21, 'James', 'USA', 5600.00, '555-666-7777'),
  (22, 'Liam', 'CAN', 5300.00, '666-777-8888'),
  (23, 'Oliver', 'USA', 6200.00, '777-888-9999'),
  (24, 'Emily', 'CAN', 4800.00, '888-999-0000'),
  (25, 'Benjamin', 'USA', 5500.00, '999-000-1111'),
  (26, 'Amelia', 'CAN', 5100.00, '000-111-2222'),
  (27, 'Henry', 'USA', 5400.00, '111-222-3333'),
  (28, 'Harper', 'CAN', 4700.00, '222-333-4444'),
  (29, 'Sebastian', 'USA', 5200.00, '333-444-5555'),
  (30, 'Evelyn', 'CAN', 4900.00, '444-555-6666'),
  (31, 'Samuel', 'USA', 5600.00, '555-666-7777'),
  (32, 'Abigail', 'CAN', 5300.00, '666-777-8888'),
  (33, 'David', 'USA', 6000.00, '777-888-9999'),
  (34, 'Elizabeth', 'CAN', 4700.00, '888-999-0000'),
  (35, 'Jackson', 'USA', 5500.00, '999-000-1111'),
  (36, 'Sofia', 'CAN', 5100.00, '000-111-2222'),
  (37, 'Joseph', 'USA', 5400.00, '111-222-3333'),
  (38, 'Chloe', 'CAN', 4800.00, '222-333-4444'),
  (39, 'Daniel', 'USA', 5200.00, '333-444-5555'),
  (40, 'Victoria', 'CAN', 4900.00, '444-555-6666'),
  (41, 'John', 'USA', 5700.00, '555-666-7777'),
  (42, 'Avery', 'CAN', 5300.00, '666-777-8888'),
  (43, 'Joshua', 'USA', 6100.00, '777-888-9999'),
  (44, 'Grace', 'CAN', 4700.00, '888-999-0000'),
  (45, 'Andrew', 'USA', 5500.00, '999-000-1111'),
  (46, 'Scarlett', 'CAN', 5100.00, '000-111-2222'),
  (47, 'Samuel', 'USA', 5400.00, '111-222-3333'),
  (48, 'Nova', 'CAN', 4800.00, '222-333-4444'),
  (49, 'William', 'USA', 5200.00, '333-444-5555'),
  (50, 'Zoe', 'CAN', 4900.00, '444-555-6666'),
  (51, 'Elijah', 'USA', 5800.00, '555-666-7777'),
  (52, 'Mila', 'CAN', 5400.00, '666-777-8888'),
  (53, 'Michael', 'USA', 6100.00, '777-888-9999'),
  (54, 'Luna', 'CAN', 4700.00, '888-999-0000'),
  (55, 'Christopher', 'USA', 5500.00, '999-000-1111'),
  (56, 'Penelope', 'CAN', 5100.00, '000-111-2222'),
  (57, 'Matthew', 'USA', 5400.00, '111-222-3333'),
  (58, 'Aria', 'CAN', 4800.00, '222-333-4444'),
  (59, 'Daniel', 'USA', 5200.00, '333-444-5555'),
  (60, 'Layla', 'CAN', 4900.00, '444-555-6666'),
  (61, 'James', 'USA', 5600.00, '555-666-7777'),
  (62, 'Ellie', 'CAN', 5200.00, '666-777-8888'),
  (63, 'Benjamin', 'USA', 6000.00, '777-888-9999'),
  (64, 'Hannah', 'CAN', 4700.00, '888-999-0000'),
  (65, 'Alexander', 'USA', 5500.00, '999-000-1111'),
  (66, 'Aurora', 'CAN', 5100.00, '000-111-2222'),
  (67, 'Ethan', 'USA', 5700.00, '111-222-3333'),
  (68, 'Nora', 'CAN', 5300.00, '222-333-4444'),
  (69, 'Joseph', 'USA', 6100.00, '333-444-5555'),
  (70, 'Ella', 'CAN', 4700.00, '444-555-6666'),
  (71, 'Samuel', 'USA', 5500.00, '555-666-7777'),
  (72, 'Lucy', 'CAN', 5200.00, '666-777-8888'),
  (73, 'Jackson', 'USA', 6000.00, '777-888-9999'),
  (74, 'Anna', 'CAN', 4800.00, '888-999-0000'),
  (75, 'Daniel', 'USA', 5400.00, '999-000-1111'),
  (76, 'Leah', 'CAN', 5100.00, '000-111-2222'),
  (77, 'David', 'USA', 5700.00, '111-222-3333'),
  (78, 'Stella', 'CAN', 5300.00, '222-333-4444'),
  (79, 'John', 'USA', 6100.00, '333-444-5555'),
  (80, 'Sophia', 'CAN', 4700.00, '444-555-6666'),
  (81, 'William', 'USA', 5500.00, '555-666-7777'),
  (82, 'Elizabeth', 'CAN', 5200.00, '666-777-8888'),
  (83, 'Oliver', 'USA', 6000.00, '777-888-9999'),
  (84, 'Ava', 'CAN', 4800.00, '888-999-0000'),
  (85, 'Henry', 'USA', 5400.00, '999-000-1111'),
  (86, 'Emma', 'CAN', 5100.00, '000-111-2222'),
  (87, 'Daniel', 'USA', 5800.00, '111-222-3333'),
  (88, 'Grace', 'CAN', 5300.00, '222-333-4444'),
  (89, 'Joseph', 'USA', 6100.00, '333-444-5555'),
  (90, 'Charlotte', 'CAN', 4700.00, '444-555-6666'),
  (91, 'Samuel', 'USA', 5500.00, '555-666-7777'),
  (92, 'Mia', 'CAN', 5200.00, '666-777-8888'),
  (93, 'Elijah', 'USA', 6000.00, '777-888-9999'),
  (94, 'Sophie', 'CAN', 4700.00, '888-999-0000'),
  (95, 'Matthew', 'USA', 5400.00, '999-000-1111'),
  (96, 'Emily', 'CAN', 5100.00, '000-111-2222'),
  (97, 'Andrew', 'USA', 5700.00, '111-222-3333'),
  (98, 'Scarlett', 'CAN', 5300.00, '222-333-4444'),
  (99, 'William', 'CAN', 6100.00, '333-444-5555'),
  (100, 'Luna', 'CAN', 5000.00, '444-555-6666');

 select * from orgdata;

 select * from orgdata where salary >=5300;

---groupby
 select phone_no, count(*) as total_users
 from orgdata
 GROUP BY phone_no;

select Salary, count(*) as total_users
from orgdata
GROUP BY Salary;

---having
select phone_no, count(*) as total_users
from orgdata
GROUP BY phone_no
HAVING count(*)>9

---order by
select name, phone_no from orgdata
ORDER BY 1 ASC,2 DESC;

---muntiple
select name, countrycode from orgdata
ORDER BY name ASC, countrycode ASC;

---using implict column
select name, countrycode from orgdata
ORDER BY 1 ASC,2 DESC;

---intersect operation
select * from student intersect