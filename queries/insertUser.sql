use challenge;
drop procedure if exists sp_InsertUser;
delimiter $$
create procedure `sp_InsertUser`(
in Email varchar(100)
)
BEGIN
insert into challenge.User (email) values (Email);
END
delimiter ;
