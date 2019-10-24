SELECT MAX(ds) FROM s1 WHERE ds NOT IN (SELECT MAX(ds) FROM s1);









.create table q1(
 rollno number(2) not null,
 fname varchar(255),
 address varchar(255),
 city varchar(255)
);

insert into q1
values (02, "Ankit","sigce","ghansoli");

create table s2( 
    rollno int(2) not null, 
    ds int(2), 
    os int(2),
    dlda int(2), 
    FOREIGN KEY(rollno) REFERENCES q1(rollno) )



SELECT rollno, fname, ds FROM q1 INNER JOIN s1 USING(rollno)


select ds, os, dlda from s1 union all select sum(ds),sum(os), sum(dlda) from s1



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
