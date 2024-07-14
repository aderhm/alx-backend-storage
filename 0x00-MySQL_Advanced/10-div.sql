-- Division function

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE division FLOAT;
    IF b = 0 THEN
        RETURN 0;
    END IF;
    SET division = a / b;
    RETURN division;
END $$

DELIMITER ;
