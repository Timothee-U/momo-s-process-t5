## JSON Data Modeling (Team Template)

Fill the following with your team’s confirmations and adjustments.

### Entities and JSON Schemas
- Confirm each schema under `schemas/` matches the current SQL:
  - `Users` → `schemas/user.schema.json`
  - `Transaction_Categories` → `schemas/transaction_category.schema.json`
  - `Transactions` → `schemas/transaction.schema.json`
  - `Transactions_Participants` → `schemas/transaction_participant.schema.json`
  - `System_Logs` → `schemas/system_log.schema.json`

### SQL → JSON field mapping (verify and adjust if needed)

- Users → User
  - `users.user_id` → `userId`
  - `users.full_name` → `fullName`
  - `users.phone_number` → `phoneNumber`
  - `users.created_at` → `createdAt`

- Transaction_Categories → TransactionCategory
  - `transaction_categories.category_id` → `categoryId`
  - `transaction_categories.name` → `name`
  - `transaction_categories.description` → `description`

- Transactions → Transaction
  - `transactions.transaction_id` → `transactionId`
  - `transactions.amount` → `amount`
  - `transactions.currency` → `currency`
  - `transactions.timestamp` → `timestamp`
  - `transactions.status` → `status`
  - `transactions.category_id` → `categoryId`

- Transactions_Participants → TransactionParticipant
  - `transactions_participants.id` → `id`
  - `transactions_participants.transaction_id` → `transactionId`
  - `transactions_participants.user_id` → `userId`
  - `transactions_participants.role` → `role`

- System_Logs → SystemLog
  - `system_logs.log_id` → `logId`
  - `system_logs.transaction_id` → `transactionId`
  - `system_logs.event_type` → `eventType`
  - `system_logs.created_at` → `createdAt`
  - `system_logs.message` → `message`

### Example API response shapes (reference)
See `examples/json_schemas.json` and `examples/transaction_full_response.example.json`.

### Team Notes
- Confirm date/time formats your API will use.
- Confirm allowed values for `status` and `role`.
- Decide whether to expose raw integer IDs or opaque IDs in public APIs.


