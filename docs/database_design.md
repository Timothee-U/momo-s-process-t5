# Database Design Document (Team Template)

## ERD
Insert your team-created ERD export (PNG/PDF) here and commit it under `docs/`.

## Rationale and Justification
- Normalize core entities: Users, Transactions, Categories, Logs.
- `Transactions_Participants` supports multi-party roles without duplicating data.
- Logs are append-only for auditability.

## Data Dictionary (summary)
- Users(user_id PK, full_name, phone_number UNIQUE, created_at)
- Transaction_Categories(category_id PK, name, description)
- Transactions(transaction_id PK, amount DECIMAL(15,2), currency CHAR(3), timestamp DATETIME, status VARCHAR(20), category_id FK)
- Transactions_Participants(id PK, transaction_id FK, user_id FK, role)
- System_Logs(log_id PK, transaction_id FK, event_type, created_at, message)

## Sample Queries (add screenshots in PDF)
```sql
-- Transactions with category name
SELECT t.transaction_id, t.amount, t.currency, t.timestamp, t.status,
       c.name AS category_name
FROM Transactions t
LEFT JOIN Transaction_Categories c ON c.category_id = t.category_id;

-- Full transaction with participants and users
SELECT t.transaction_id, u.full_name, p.role
FROM Transactions t
JOIN Transactions_Participants p ON p.transaction_id = t.transaction_id
JOIN Users u ON u.user_id = p.user_id
WHERE t.transaction_id = 1;

-- Logs for a transaction
SELECT l.* FROM System_Logs l WHERE l.transaction_id = 1 ORDER BY l.created_at;
```

## Unique Rules / Integrity (document and include screenshots)
- `users.phone_number` must be unique.
- `transactions.status` constrained to application-level enum: PENDING|COMPLETED|FAILED.
- Foreign keys enforce referential integrity across entities.

## JSON Representations
See `docs/json_modeling.md` and `examples/` for shapes and samples.


