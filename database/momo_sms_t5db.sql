CREATE DATABASE IF NOT EXISTS momo_sms_t5db;
USE momo_sms_t5db;
SELECT DATABASE();
CREATE TABLE Users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(15) NOT NULL UNIQUE,
  created_at Timestamp DEFAULT CURRENT_TIMESTAMP
);
SELECT DATABASE();

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
    FOREIGN KEY (category_id) REFERENCES Transaction_categories (category_id)
);

CREATE TABLE System_Logs (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  transaction_id INT,
  event_type VARCHAR(50) NOT NULL,
  Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  message TEXT,
  FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id)
);

SELECT * FROM System_Logs;
DROP TABLE IF EXISTS System_Logs;

CREATE TABLE System_Logs (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  transaction_id INT,
  event_type VARCHAR(50) NOT NULL,
  Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  message TEXT,
  FOREIGN KEY (transaction_id) REFERENCES Transactions (transaction_id)
);
SHOW TABLES;
RENAME TABLE users TO Users;
DESCRIBE system_logs;
DESCRIBE Transactions;
DESCRIBE Transaction_Categories;
DESCRIBE users;
CREATE TABLE Transactions_Participants (
    id             INT PRIMARY KEY AUTO_INCREMENT,
    transaction_id INT         NOT NULL,
    user_id        INT         NOT NULL,
    role           VARCHAR(50) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES Transactions (transaction_id),
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);
DESCRIBE Transactions_Participants;
SHOW TABLES;
DESCRIBE Transactions_Participants;
DESCRIBE System_Logs;
INSERT INTO users (full_name, phonenumber) VALUES ('Naomi', '0788553245'), ('Oladimeji', '0791204732');
INSERT INTO transaction_categories (name, description) VALUES ('Food', 'Food purchases');
SELECT * FROM TRANSACTIONS;
INSERT INTO users (full_name, phonenumber) VALUES ('Timothee', '0791504721');
INSERT INTO momo_sms_t5db.Transaction_Categories (name, description) VALUES ('Transport', 'Transport Charges');
INSERT INTO transactions (amount, currency, timestamp, category_id) VALUES (15000, 'RWF', NOW(), 1), (23000, 'RWF', NOW(), 2);
SELECT * FROM TRANSACTIONS;
SELECT * FROM Transaction_Categories;
SELECT * FROM Transactions_Participants;
SELECT * FROM users;
DELETE FROM transactions WHERE transaction_id IN (1,2);
INSERT INTO transactions (amount, currency, timestamp, category_id) VALUES (12500, 'RWF', NOW(), 1), (35200, 'RWF', NOW(), 2);
SELECT * FROM TRANSACTIONS;
INSERT INTO Transactions_Participants (transaction_id, user_id, role) VALUES (3, 1, 'payer'),
                                                                             (3,2, 'receiver'),
                                                                             (4, 2, 'payer'),
                                                                             (4, 3, 'receiver'),
                                                                             (5, 1, 'payer'),
                                                                             (5, 3, 'receive'),
                                                                             (6,3, 'payer'),
                                                                             (6, 1, 'receiver');
DROP TABLE IF EXISTS Transactions_Participants;
CREATE TABLE Transactions_Participants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_id INT NOT NULL,
    user_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
INSERT INTO Transactions_Participants (transaction_id, user_id, role) VALUES
(3, 1, 'payer'),
(3, 2, 'receiver'),
(4, 2, 'payer'),
(4, 3, 'receiver'),
(5, 1, 'payer'),
(5, 3, 'receiver'),
(6, 3, 'payer'),
(6, 1, 'receiver');
SELECT * FROM momo_sms_t5db.Transactions_Participants;
SELECT * FROM Users;
SELECT * FROM System_Logs;
SELECT * FROM Transactions;
SELECT * FROM Transaction_Categories;
INSERT INTO System_Logs (transaction_id, event_type, message) VALUES
(3, 'Transaction created', 'Transaction 3 Successfully initiated'),
(4, 'Transaction created', 'Transaction 4 Successfully initiated'),
(5, 'Transaction created', 'Transaction 5 Successfully initiated'),
(6, 'Transaction created', 'Transaction 6 Successfully initiated');
SELECT t.transaction_id, t.amount, t.currency, u.full_name, tp.role
FROM Transactions t
JOIN Transactions_Participants tp ON t.transaction_id = tp.transaction_id
JOIN Users u ON tp.user_id = u.user_id
ORDER BY t.transaction_id;
SELECT * FROM System_Logs ORDER BY transaction_id, Created_at;
UPDATE Transactions
SET status = 'PENDING'
WHERE status = 'INITIATED';
SELECT t.transaction_id, t.amount, t.currency, u.full_name, tp.role
FROM Transactions t
JOIN Transactions_Participants tp ON t.transaction_id = tp.transaction_id
JOIN Users u ON tp.user_id = u.user_id
ORDER BY t.transaction_id;
SELECT t.transaction_id, t.amount, t.status, s.event_type, s.message, s.Created_at
FROM Transactions t
LEFT JOIN System_Logs s ON t.transaction_id = s.transaction_id
ORDER BY t.transaction_id, s.Created_at;