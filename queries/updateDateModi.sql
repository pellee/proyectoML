USE challenge;
DROP procedure IF EXISTS sp_UpdateDateModi;

delimiter $$
CREATE PROCEDURE `sp_UpdateDateModi` (

DateModi datetime,
idF varchar(150)
)
BEGIN

update challenge.usrdata set dateModi=DateModi where idFile=idF;

END

delimiter ;
