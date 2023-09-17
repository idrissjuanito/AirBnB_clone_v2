-- Creates a test database for the airbnb project
CREATE DATABASE hbnb_test_db;
-- Creates a test user
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Assigns privileges for the airbnb project db to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
