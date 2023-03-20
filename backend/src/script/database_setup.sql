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