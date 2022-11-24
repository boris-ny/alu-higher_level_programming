-- converts hbtcn database to utf8,collate utf8_unicode_ci
ALTER DATABASE hbtn_0c_0 
CHARACTER SET utf8 
COLLATE utf8_unicode_ci;

ALTER TABLE first_table 
IN DATABASE hbtn_0c_0 
CONVERT TO CHARACTER SET utf8 
COLLATE utf8_unicode_ci;
