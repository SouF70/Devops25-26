CREATE DATABASE IF NOT EXISTS devopsdb;

USE devopsdb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL
);

INSERT INTO users (username, role) VALUES
('admin', 'administrator'),
('student', 'user');