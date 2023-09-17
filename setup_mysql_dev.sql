-- Creates a database for the airbnb project
CREATE DATABASE hbnb_dev_db;
-- Creates a user
CREATE USER ‘hbnb_dev’@’localhost’ IDENTIFIED BY 'hbnb_dev_pwd';
-- Assigns privileges for the airbnb project db to user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
GRANT SELECT ON performance_schema TO `hbnb_dev`@`localhost`;
