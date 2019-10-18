# Customer-Information-System
Customer Information System form with DB (GUI) in python 
Tkinter
SQLite



CREATE TABLE Persons(
    FName varchar(255),
    PersonID int not null PRIMARY KEY,
    bdate date,
    address varchar(255),
    sex varchar(5),
    salary int
);


INSERT INTO Persons
VALUES ("sanket", 01, 1999-12-25, "ghansoli", "m", 500);



CREATE TABLE Persons(
    FName varchar(255),
    PersonID int not null PRIMARY KEY,
    bdate date,
    address varchar(255),
    sex varchar(5),
    salary int
);



INSERT INTO Persons
VALUES ("sanket", 01, "1999/12/25", "ghansoli", "m", 500);


INSERT INTO Persons
VALUES ("sanket", 02, "1999/12/25", "ghansoli", "m", 500);


INSERT INTO Persons
VALUES ("sanket", 03, "1999/12/25", "ghansoli", "m", 500);


select *  from persons
