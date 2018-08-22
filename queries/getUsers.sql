USE challenge;
DROP procedure IF EXISTS sp_GetAllUsers;

delimiter $$
CREATE PROCEDURE `sp_GetAllUsers` ()

BEGIN

select email from challenge.user;

END

delimiter ;
