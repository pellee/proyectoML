USE challenge;
DROP procedure IF EXISTS sp_GetFilesName;

delimiter $$
CREATE PROCEDURE `sp_GetFilesName` (

Ownnr varchar(100)
)
BEGIN

select nameFile, idFile from challenge.usrdata where ownr = Ownnr;

END

delimiter ;
