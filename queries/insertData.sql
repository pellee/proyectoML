use challenge;
drop procedure if exists sp_InsertData;
delimiter $$
create procedure `sp_InsertData`(
in IdFile varchar (150),
in NameFile varchar (75),
in Extension varchar (5),
in Ownr varchar (100),
in Visibility bit,
in DateModi datetime
)
BEGIN
insert into challenge.usrdata (idFile, nameFile, extension, ownr, visibility, dateModi)
values (IdFile, NameFile, Extension, Ownr, Visibility, DateModi);
END
delimiter ;
