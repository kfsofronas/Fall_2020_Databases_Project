DROP TABLE car CASCADE CONSTRAINTS;
CREATE TABLE car (
	VIN			char(17) not null, 
	Model_ID		char(15) not null,
	Dealership_ID		char(10) not null,
	Salesperson_ID	char(15) not null,
	Registration_Num	varchar(15),
	NewOrUsed		varchar(4),
	AskingPrice		integer,
	Mileage		integer,
	Color			varchar(10),
	primary key(VIN)
);

DROP TABLE car_model CASCADE CONSTRAINTS;
CREATE TABLE car_model (
	Model_ID		char(15) not null,
	Model_Name		varchar(30),
Manufacturer		varchar(20),
	Body_Style		varchar(20),
	Drive_Type		char(3),
	Year			integer,
	Transmission    	varchar(30),
	Engine			varchar(30),
	Fuel			varchar(20),
	MPG_City		integer,
	MPG_Highway		integer,
	primary key(Model_ID)
);

ALTER TABLE car ADD (
foreign key (Model_ID) references car_model(Model_ID)
);

DROP TABLE owner CASCADE CONSTRAINTS;
CREATE TABLE owner (
	Owner_ID		char(10) not null,
	VIN			char(17) not null, 
	fname			varchar(15),
	lname			varchar(15),
	Year_Acquired		integer,
	Year_Sold		integer,
	primary key(Owner_ID),
	foreign key(VIN) references car(VIN)
);

DROP TABLE dealership CASCADE CONSTRAINTS;
CREATE TABLE dealership (
	Dealership_ID		char(10) not null,      
	Dealership_Name	varchar(30),
	Dealership_Address	varchar(50),
	Phone_Number		integer,
	Website		varchar(20),
	primary key(Dealership_ID)
);
ALTER TABLE car ADD (
foreign key (Dealership_ID) references dealership(Dealership_ID)
);


DROP TABLE salesperson CASCADE CONSTRAINTS;
CREATE TABLE salesperson (
	Employee_ID		char(15) not null,           
	fname			varchar(15),
	lname			varchar(15),
	Dealership_ID		char(10) not null,  
	Employee_Phone	integer,
	Email			varchar(40),
	primary key(Employee_ID),
	foreign key(Dealership_ID) references dealership(Dealership_ID)
);

ALTER TABLE car ADD (
foreign key (Salesperson_ID) references salesperson(Employee_ID)
);

DROP TABLE accident_history CASCADE CONSTRAINTS;
CREATE TABLE accident_history (
	Accident_ID		char(10) not null,
	VIN			char(17) not null,           
	Owner_ID		char(10) not null,
	Damage_Severity	varchar(8),           -- mild/moderate/severe
	Description		varchar(100),
	primary key(Accident_ID),
	foreign key(VIN) references car(VIN),
	foreign key(Owner_ID) references owner(Owner_ID)
);
