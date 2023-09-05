CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS cpu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value FLOAT
);

CREATE TABLE IF NOT EXISTS mem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value FLOAT
);

CREATE TABLE IF NOT EXISTS disk (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value FLOAT
);


SHOW TABLES;
