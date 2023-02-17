-- Scripts for setting up environment
-- Use as a reference instead of automated procedure

-- Create user with credentials
CREATE USER 'yw'@'localhost' IDENTIFIED BY 't3iMfiRVm6';

-- Create schema with utf8mb4 character set
CREATE SCHEMA travel CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE travel;

-- Create article table
CREATE TABLE article (
  id int NOT NULL AUTO_INCREMENT,
  title VARCHAR(200),
  content MEDIUMTEXT,
  created_on DATETIME DEFAULT CURRENT_TIMESTAMP,
  last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;