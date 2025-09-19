CREATE DATABASE IF NOT EXISTS momo_sms_t5db;
USE momo_sms_t5db;
CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(15) NOT NULL UNIQUE,
  created_at Timestamp DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Transaction_Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT
);
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(15,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'RWF',
    timestamp DATETIME NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING',
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Transaction_Categories (category_id)
);
CREATE TABLE System_Logs (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  transaction_id INT,
  event_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  message TEXT,
  FOREIGN KEY (transaction_id) REFERENCES Transactions (transaction_id)
);
INSERT INTO users (full_name, phone_number) VALUES ('Naomi', '0788553245'), ('Oladimeji', '0791204732');
INSERT INTO transaction_categories (name, description) VALUES ('Food', 'Food purchases'), ('Transport', 'Transport Charges');
INSERT INTO users (full_name, phone_number) VALUES ('Timothee', '0791504721');
INSERT INTO transactions (amount, currency, timestamp, category_id) VALUES (15000, 'RWF', NOW(), 1), (23000, 'RWF', NOW(), 2);
INSERT INTO transactions (amount, currency, timestamp, category_id) VALUES (12500, 'RWF', NOW(), 1), (35200, 'RWF', NOW(), 2);
CREATE TABLE Transactions_Participants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_id INT NOT NULL,
    user_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
INSERT INTO Transactions_Participants (transaction_id, user_id, role) VALUES
(1, 1, 'payer'),
(1, 2, 'receiver'),
(2, 2, 'payer'),
(2, 3, 'receiver'),
(3, 1, 'payer'),
(3, 3, 'receiver'),
(4, 3, 'payer'),
(4, 1, 'receiver');
INSERT INTO System_Logs (transaction_id, event_type, message) VALUES
(1, 'Transaction created', 'Transaction 1 Successfully initiated'),
(2, 'Transaction created', 'Transaction 2 Successfully initiated'),
(3, 'Transaction created', 'Transaction 3 Successfully initiated'),
(4, 'Transaction created', 'Transaction 4 Successfully initiated');
