-- Scripts for setting up database
-- Use as a reference instead of automated procedure

-- Create user with credentials
CREATE USER 'yw'@'localhost' IDENTIFIED BY 't3iMfiRVm6';

-- Grant privileges from the root account
-- GRANT ALL PRIVILEGES ON *.* TO `yw`@`localhost`;

-- Create schema with utf8mb4 character set
CREATE SCHEMA travel CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE travel;

-- SQLAlchemy will create the table for you
-- Thus the following commands are not necessary

-- Create article table
CREATE TABLE article (
  id int NOT NULL AUTO_INCREMENT,
  title VARCHAR(200),
  content LONGTEXT,
  created_on DATETIME DEFAULT CURRENT_TIMESTAMP,
  last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user table
CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(200),
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  title VARCHAR(100),
  email VARCHAR(100),
  updated DATETIME DEFAULT CURRENT_TIMESTAMP,
  deleted BOOLEAN DEFAULT 0,
  PRIMARY KEY (id)
 ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;