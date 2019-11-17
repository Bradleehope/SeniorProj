-- Create a new datClothes
-- Connect to the 'master' database to run this snippet
USE master
GO

CREATE TABLE shirt (
id INT PRIMARY KEY,
nickname TEXT UNIQUE  NOT NULL,
primary_color TEXT NOT NULL,
second_color TEXT,

-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'Clothes'
)
CREATE DATABASE Clothes
GO

CREATE TABLE shirt (
id INT PRIMARY KEY,
nickname TEXT UNIQUE NOT NULL,
primary_color TEXT NOT NULL,
second_color TEXT,
style TEXT NOT NULL,
occasion TEXT NOT NULL,
weather TEXT NOT NULL,
holiday TEXT,
fit TEXT,
description_input TEXT,
image_link URL NOT NULL
)
