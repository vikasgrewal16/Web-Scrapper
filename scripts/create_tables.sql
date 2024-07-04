CREATE DATABASE website_info;

USE website_info;

CREATE TABLE website_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    contact_email VARCHAR(255),
    contact_address TEXT,
    contact_number VARCHAR(50),
    language VARCHAR(50),
    cms_mvc VARCHAR(100),
    category VARCHAR(100)
);
