-- Create the force_name table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
