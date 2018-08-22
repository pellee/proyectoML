create database if not exists Challenge;

use Challenge;

create table User(

id int not null auto_increment,
email varchar (100) not null,

primary key (id)

);

create table UsrData(

id int not null auto_increment,
idFile varchar (150) not null,
nameFile varchar (75) not null,
extension varchar (5) not null,
ownr varchar (100) not null,
visibility bit not null,
dateModi datetime not null,

primary key (id)

);
